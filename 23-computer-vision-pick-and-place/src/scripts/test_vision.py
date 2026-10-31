"""Unit tests for Computer Vision Pick-and-Place and coordinate transforms."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from vision_pick_and_place import VisionPickAndPlaceEngine


def test_pinhole_backprojection():
    # fx = 500, fy = 500, cx = 320, cy = 240
    K = np.array([
        [500.0,   0.0, 320.0],
        [  0.0, 500.0, 240.0],
        [  0.0,   0.0,   1.0]
    ])
    T_eye = np.eye(4)
    engine = VisionPickAndPlaceEngine(K, T_eye)

    # Pixel right at optical center: (320, 240) at depth 500 mm
    # Should project to (0, 0, 500) mm in camera frame
    p_cam = engine.pixel_and_depth_to_camera_point(320.0, 240.0, depth_mm=500.0)
    assert np.allclose(p_cam, [0.0, 0.0, 500.0], atol=1e-5)

    # Pixel shifted by +50 px in u: (370, 240) at depth 500 mm
    # X = (370 - 320) * 500 / 500 = 50.0 mm
    p_cam_offset = engine.pixel_and_depth_to_camera_point(370.0, 240.0, depth_mm=500.0)
    assert np.allclose(p_cam_offset, [50.0, 0.0, 500.0], atol=1e-5)


def test_grasp_transformation_chain():
    K = np.eye(3)
    # Hand-eye offset: camera is 50mm in front of flange (X+50)
    T_flange_cam = np.eye(4)
    T_flange_cam[0, 3] = 50.0

    engine = VisionPickAndPlaceEngine(K, T_flange_cam)

    # Robot flange is at (400, 0, 300) in Base
    T_base_flange = np.eye(4)
    T_base_flange[:3, 3] = [400.0, 0.0, 300.0]

    # Object is 200mm in front of camera (Z+200)
    p_obj_cam = np.array([0.0, 0.0, 200.0])

    T_base_obj = engine.compute_grasp_pose_in_base(T_base_flange, p_obj_cam)
    # Target X = 400 + 50 = 450; Target Z = 300 + 200 = 500
    assert np.allclose(T_base_obj[:3, 3], [450.0, 0.0, 500.0], atol=1e-4)
