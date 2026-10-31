"""Unit tests for ROS2 hardware interface and quintic polynomial trajectory."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from kuka_ros2_interface import QuinticTrajectoryInterpolator, KukaRos2HardwareBridge


def test_quintic_boundary_conditions():
    p0, p1 = 0.5, 2.0
    duration = 3.0
    traj = QuinticTrajectoryInterpolator.sample_trajectory(p0, p1, duration_sec=duration)

    # Position at endpoints
    assert np.isclose(traj["position"][0], p0, atol=1e-4)
    assert np.isclose(traj["position"][-1], p1, atol=1e-4)

    # Velocity at endpoints must be zero
    assert np.isclose(traj["velocity"][0], 0.0, atol=1e-4)
    assert np.isclose(traj["velocity"][-1], 0.0, atol=1e-4)

    # Acceleration at endpoints must be zero
    assert np.isclose(traj["acceleration"][0], 0.0, atol=1e-4)
    assert np.isclose(traj["acceleration"][-1], 0.0, atol=1e-4)


def test_ros2_hardware_bridge_state_update():
    bridge = KukaRos2HardwareBridge()
    state0 = bridge.read_joint_state(timestamp=0.0)
    assert len(state0.names) == 6
    assert np.allclose(state0.positions_rad, 0.0)

    # Command move
    target = np.array([0.1, -0.5, 0.8, 0.0, 0.2, -0.1])
    bridge.write_joint_commands(target, dt=0.02)

    state1 = bridge.read_joint_state(timestamp=0.02)
    assert np.allclose(state1.positions_rad, target)
    assert np.allclose(state1.velocities_rad_s, target / 0.02)
