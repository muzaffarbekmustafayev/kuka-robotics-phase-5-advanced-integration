"""Unit tests for C-Space RRT Motion Planner."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from cspace_rrt_planner import CSpaceRRTPlanner


def test_free_space_planning():
    q_min = np.full(6, -np.pi)
    q_max = np.full(6, np.pi)
    planner = CSpaceRRTPlanner(q_min, q_max, step_size_rad=0.3, seed=123)

    q_start = np.zeros(6)
    q_goal = np.array([0.5, -0.5, 0.5, 0.0, 0.0, 0.0])

    path = planner.plan(q_start, q_goal, max_iter=500)

    assert path is not None
    assert len(path) >= 2
    assert np.allclose(path[0], q_start, atol=1e-4)
    assert np.allclose(path[-1], q_goal, atol=1e-4)


def test_obstacle_avoidance():
    q_min = np.full(6, -np.pi)
    q_max = np.full(6, np.pi)
    planner = CSpaceRRTPlanner(q_min, q_max, step_size_rad=0.2, goal_bias=0.3, seed=42)

    # Localized obstacle blocking the straight line at origin
    obs_low = np.array([-0.2, -0.2, -0.2, -0.2, -0.2, -0.2])
    obs_high = np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
    planner.add_obstacle_box(obs_low, obs_high)

    q_start = np.array([-0.6, 0.0, 0.0, 0.0, 0.0, 0.0])
    q_goal = np.array([0.6, 0.0, 0.0, 0.0, 0.0, 0.0])

    path = planner.plan(q_start, q_goal, max_iter=2500)

    assert path is not None
    # Verify every point in path does not collide with obstacle
    for pt in path:
        assert planner.is_collision_free(pt)
