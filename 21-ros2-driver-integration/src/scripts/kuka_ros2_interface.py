"""ROS2 Hardware Interface & FollowJointTrajectory Controller for KUKA KR 6.

Simulates ROS2 JointState message publishing, 5th-order (quintic) polynomial
trajectory interpolation, and real-time command streaming to the KUKA robot.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
import numpy as np


@dataclass
class RosJointState:
    """Represents standard ROS2 sensor_msgs/msg/JointState."""
    names: List[str]
    positions_rad: np.ndarray
    velocities_rad_s: np.ndarray
    effort_nm: np.ndarray
    timestamp_sec: float


class QuinticTrajectoryInterpolator:
    r"""Calculates minimum-jerk 5th-order polynomial trajectory:

    s(t) = a0 + a1*t + a2*t^2 + a3*t^3 + a4*t^4 + a5*t^5
    Satisfying: s(0)=p0, s(T)=p1, s_dot(0)=v0, s_dot(T)=v1, s_ddot(0)=a0, s_ddot(T)=a1.
    """

    @staticmethod
    def compute_coefficients(p0: float, p1: float, v0: float, v1: float, a0: float, a1: float, T: float) -> np.ndarray:
        """Solve 6x6 linear system for quintic polynomial coefficients."""
        if T <= 0.0:
            raise ValueError("Duration T must be positive.")

        A = np.array([
            [1.0, 0.0, 0.0,      0.0,        0.0,        0.0],
            [0.0, 1.0, 0.0,      0.0,        0.0,        0.0],
            [0.0, 0.0, 2.0,      0.0,        0.0,        0.0],
            [1.0, T,   T**2,     T**3,       T**4,       T**5],
            [0.0, 1.0, 2.0 * T,  3.0 * T**2, 4.0 * T**3, 5.0 * T**4],
            [0.0, 0.0, 2.0,      6.0 * T,    12.0 * T**2,20.0 * T**3]
        ])
        b = np.array([p0, v0, a0, p1, v1, a1])
        coeffs = np.linalg.solve(A, b)
        return coeffs

    @classmethod
    def sample_trajectory(cls, p0: float, p1: float, duration_sec: float, dt: float = 0.01) -> Dict[str, np.ndarray]:
        """Sample smooth quintic position, velocity, and acceleration profile."""
        coeffs = cls.compute_coefficients(p0, p1, v0=0.0, v1=0.0, a0=0.0, a1=0.0, T=duration_sec)
        times = np.arange(0.0, duration_sec + dt, dt)

        pos, vel, acc = [], [], []
        c = coeffs
        for t in times:
            p = c[0] + c[1]*t + c[2]*t**2 + c[3]*t**3 + c[4]*t**4 + c[5]*t**5
            v = c[1] + 2*c[2]*t + 3*c[3]*t**2 + 4*c[4]*t**3 + 5*c[5]*t**4
            a = 2*c[2] + 6*c[3]*t + 12*c[4]*t**2 + 20*c[5]*t**3
            pos.append(p)
            vel.append(v)
            acc.append(a)

        return {
            "time": times,
            "position": np.array(pos),
            "velocity": np.array(vel),
            "acceleration": np.array(acc),
        }


class KukaRos2HardwareBridge:
    """Bridges ROS2 controller commands with KUKA KR 6 joint state telemetry."""

    JOINT_NAMES = [f"joint_a{i}" for i in range(1, 7)]

    def __init__(self):
        self.current_joints_rad = np.zeros(6, dtype=np.float64)
        self.current_vel_rad = np.zeros(6, dtype=np.float64)

    def read_joint_state(self, timestamp: float) -> RosJointState:
        """Produce ROS2 JointState message."""
        return RosJointState(
            names=list(self.JOINT_NAMES),
            positions_rad=self.current_joints_rad.copy(),
            velocities_rad_s=self.current_vel_rad.copy(),
            effort_nm=np.zeros(6),
            timestamp_sec=timestamp,
        )

    def write_joint_commands(self, target_joints_rad: np.ndarray, dt: float):
        """Simulate sending position setpoints to KUKA drive hardware."""
        targets = np.asarray(target_joints_rad, dtype=np.float64)
        self.current_vel_rad = (targets - self.current_joints_rad) / dt
        self.current_joints_rad = targets.copy()


def main():
    print("=" * 65)
    print("Lesson 21: ROS2 Hardware Interface & Quintic Trajectory Solver")
    print("=" * 65)

    bridge = KukaRos2HardwareBridge()
    interpolator = QuinticTrajectoryInterpolator()

    # Move Axis 1 from 0.0 rad to 1.57 rad (90 deg) in 2.0 seconds
    traj = interpolator.sample_trajectory(p0=0.0, p1=np.pi/2, duration_sec=2.0)

    print(f"\nInterpolated Quintic Trajectory for Joint 1:")
    print(f"  Duration: 2.00 s")
    print(f"  Initial Pos: {traj['position'][0]:.4f} rad, Final Pos: {traj['position'][-1]:.4f} rad")
    print(f"  Peak Vel:    {np.max(traj['velocity']):.4f} rad/s")
    print(f"  Start/End Velocity: {traj['velocity'][0]:.4f} / {traj['velocity'][-1]:.4f} rad/s (Smooth Jerk-Free)")


if __name__ == "__main__":
    main()
