"""Computer Vision, Hand-Eye Calibration (AX = XB) & Pick-and-Place Engine.

Implements Tsai-Lenz Hand-Eye calibration solver, pinhole camera projection,
and coordinate transformation chaining from 2D pixel detections to KUKA Base frame grasp poses:
    T_base_obj = T_base_flange * T_flange_cam * T_cam_obj
"""

from typing import Tuple, Dict, Optional
import numpy as np


class VisionPickAndPlaceEngine:
    r"""Calculates 3D grasping poses from camera observations and hand-eye transformations."""

    def __init__(self,
                 camera_matrix_k: np.ndarray,
                 t_flange_cam: np.ndarray):
        """
        Args:
            camera_matrix_k: 3x3 intrinsic matrix [[fx, 0, cx], [0, fy, cy], [0, 0, 1]].
            t_flange_cam: 4x4 eye-in-hand transformation matrix from flange to camera.
        """
        self.K = np.asarray(camera_matrix_k, dtype=np.float64)
        self.K_inv = np.linalg.inv(self.K)
        self.T_flange_cam = np.asarray(t_flange_cam, dtype=np.float64)

    def pixel_and_depth_to_camera_point(self, u_px: float, v_px: float, depth_mm: float) -> np.ndarray:
        r"""Back-project 2D pixel (u, v) and measured depth Z into 3D camera coordinate [X_c, Y_c, Z_c].

        [X_c, Y_c, 1]^T = Z * K^-1 * [u, v, 1]^T
        """
        pixel_homo = np.array([u_px, v_px, 1.0], dtype=np.float64)
        normalized_ray = self.K_inv @ pixel_homo
        return normalized_ray * depth_mm

    def compute_grasp_pose_in_base(self,
                                   t_base_flange: np.ndarray,
                                   p_obj_in_cam: np.ndarray,
                                   r_obj_in_cam: Optional[np.ndarray] = None) -> np.ndarray:
        r"""Compute 4x4 grasp matrix T_base_obj:

        T_base_obj = T_base_flange @ T_flange_cam @ T_cam_obj
        """
        if r_obj_in_cam is None:
            r_obj_in_cam = np.eye(3)

        T_cam_obj = np.eye(4, dtype=np.float64)
        T_cam_obj[:3, :3] = r_obj_in_cam
        T_cam_obj[:3, 3] = p_obj_in_cam

        T_base_obj = t_base_flange @ self.T_flange_cam @ T_cam_obj
        return T_base_obj

    @staticmethod
    def solve_tsai_lenz_rotation(R_a_list: list, R_b_list: list) -> np.ndarray:
        r"""Solve AX = XB rotation component using Tsai-Lenz formulation.

        skew(k_A + k_B) * P_x = 2 * (k_A - k_B)
        where k_A and k_B are axis-angle vectors.
        """
        # Linear system A_mat * x = b_vec
        A_rows = []
        b_rows = []

        for Ra, Rb in zip(R_a_list, R_b_list):
            # Log map to get rotation vectors
            from scipy.spatial.transform import Rotation
            # Fallback simple axis calculation
            tr_a = np.clip((np.trace(Ra) - 1.0) / 2.0, -1.0, 1.0)
            th_a = np.arccos(tr_a)
            if th_a > 1e-4:
                ka = (th_a / (2.0 * np.sin(th_a))) * np.array([Ra[2, 1] - Ra[1, 2], Ra[0, 2] - Ra[2, 0], Ra[1, 0] - Ra[0, 1]])
            else:
                ka = np.zeros(3)

            tr_b = np.clip((np.trace(Rb) - 1.0) / 2.0, -1.0, 1.0)
            th_b = np.arccos(tr_b)
            if th_b > 1e-4:
                kb = (th_b / (2.0 * np.sin(th_b))) * np.array([Rb[2, 1] - Rb[1, 2], Rb[0, 2] - Rb[2, 0], Rb[1, 0] - Rb[0, 1]])
            else:
                kb = np.zeros(3)

            k_sum = ka + kb
            K_skew = np.array([
                [0.0, -k_sum[2], k_sum[1]],
                [k_sum[2], 0.0, -k_sum[0]],
                [-k_sum[1], k_sum[0], 0.0]
            ])
            A_rows.append(K_skew)
            b_rows.append(2.0 * (ka - kb))

        A_mat = np.vstack(A_rows)
        b_mat = np.concatenate(b_rows)
        p_x, _, _, _ = np.linalg.lstsq(A_mat, b_mat, rcond=None)

        # Convert Rodrigues vector p_x back to rotation matrix
        norm_px = np.linalg.norm(p_x)
        if norm_px < 1e-6:
            return np.eye(3)
        P_skew = np.array([
            [0.0, -p_x[2], p_x[1]],
            [p_x[2], 0.0, -p_x[0]],
            [-p_x[1], p_x[0], 0.0]
        ])
        R_x = np.eye(3) + (2.0 / (1.0 + norm_px**2)) * (P_skew + P_skew @ P_skew)
        return R_x


def main():
    print("=" * 65)
    print("Lesson 23: Computer Vision & Hand-Eye Calibration (Pick & Place)")
    print("=" * 65)

    # Intrinsic matrix K (f = 600 px, cx = 320 px, cy = 240 px)
    K = np.array([
        [600.0,   0.0, 320.0],
        [  0.0, 600.0, 240.0],
        [  0.0,   0.0,   1.0]
    ])

    # Hand-eye offset: Camera mounted +50 mm in X, +100 mm in Z from Flange
    T_flange_cam = np.eye(4)
    T_flange_cam[:3, 3] = [50.0, 0.0, 100.0]

    engine = VisionPickAndPlaceEngine(K, T_flange_cam)

    # Robot currently at Base pose
    T_base_flange = np.eye(4)
    T_base_flange[:3, 3] = [400.0, -100.0, 450.0]

    # Vision detection: object at pixel (420, 290) with depth 400 mm
    p_cam = engine.pixel_and_depth_to_camera_point(u_px=420.0, v_px=290.0, depth_mm=400.0)
    print(f"\nObject in Camera Frame: [{p_cam[0]:.2f}, {p_cam[1]:.2f}, {p_cam[2]:.2f}] mm")

    # Grasp pose in Robot Base Frame
    T_base_obj = engine.compute_grasp_pose_in_base(T_base_flange, p_cam)
    p_grasp = T_base_obj[:3, 3]
    print(f"Grasp Pose in Robot Base Frame:")
    print(f"  X = {p_grasp[0]:.2f} mm")
    print(f"  Y = {p_grasp[1]:.2f} mm")
    print(f"  Z = {p_grasp[2]:.2f} mm")


if __name__ == "__main__":
    main()
