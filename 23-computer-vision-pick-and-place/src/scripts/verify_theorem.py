import numpy as np

def test_hand_eye_synthetic():
    # Unknown Hand-Eye matrix X (Flange to Camera)
    R_X_true = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=float)
    t_X_true = np.array([50.0, -30.0, 120.0])
    
    # Arbitrary robot movement A
    R_A = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], dtype=float)
    t_A = np.array([200.0, 100.0, -50.0])
    
    # Derived camera movement B = X^-1 @ A @ X
    R_B = R_X_true.T @ R_A @ R_X_true
    t_B = R_X_true.T @ (R_A @ t_X_true + t_A - t_X_true)
    
    # Verification of AX = XB
    T_A = np.eye(4); T_A[:3, :3] = R_A; T_A[:3, 3] = t_A
    T_B = np.eye(4); T_B[:3, :3] = R_B; T_B[:3, 3] = t_B
    T_X = np.eye(4); T_X[:3, :3] = R_X_true; T_X[:3, 3] = t_X_true
    
    assert np.allclose(T_A @ T_X, T_X @ T_B)
    print("[SUCCESS] Hand-Eye AX = XB calibration theorem verified!")

if __name__ == "__main__":
    test_hand_eye_synthetic()
