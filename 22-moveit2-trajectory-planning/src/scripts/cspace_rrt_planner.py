"""C-Space RRT (Rapidly-exploring Random Tree) Motion Planner with Collision Avoidance.

Implements collision checking in joint space C = R^6, tree expansion,
goal-biasing, and trajectory shortcut smoothing (similar to MoveIt2 / OMPL).
"""

from typing import List, Tuple, Optional
import numpy as np


class CSpaceRRTPlanner:
    r"""Rapidly-exploring Random Tree motion planner in 6-DOF joint space."""

    def __init__(self,
                 q_min: np.ndarray,
                 q_max: np.ndarray,
                 step_size_rad: float = 0.15,
                 goal_bias: float = 0.20,
                 seed: Optional[int] = 42):
        self.q_min = np.asarray(q_min, dtype=np.float64)
        self.q_max = np.asarray(q_max, dtype=np.float64)
        self.step_size = step_size_rad
        self.goal_bias = goal_bias
        self.obstacles: List[Tuple[np.ndarray, np.ndarray]] = []  # Bounding boxes in C-space [low, high]
        self.rng = np.random.default_rng(seed)

    def add_obstacle_box(self, low: np.ndarray, high: np.ndarray):
        """Add an obstacle box in C-space."""
        self.obstacles.append((np.asarray(low, dtype=np.float64), np.asarray(high, dtype=np.float64)))

    def is_collision_free(self, q: np.ndarray) -> bool:
        """Verify whether configuration q is free from collisions with obstacles."""
        for low, high in self.obstacles:
            if np.all(q >= low) and np.all(q <= high):
                return False
        return True

    def is_segment_free(self, q1: np.ndarray, q2: np.ndarray, num_checks: int = 10) -> bool:
        """Check discrete interpolation steps between q1 and q2 for collisions."""
        for alpha in np.linspace(0.0, 1.0, num_checks):
            q_interp = (1.0 - alpha) * q1 + alpha * q2
            if not self.is_collision_free(q_interp):
                return False
        return True

    def plan(self, q_start: np.ndarray, q_goal: np.ndarray, max_iter: int = 1000) -> Optional[List[np.ndarray]]:
        """Find a collision-free path from q_start to q_goal using RRT."""
        q_s = np.asarray(q_start, dtype=np.float64)
        q_g = np.asarray(q_goal, dtype=np.float64)

        if not self.is_collision_free(q_s) or not self.is_collision_free(q_g):
            return None

        # Nodes list: store (config, parent_index)
        nodes: List[np.ndarray] = [q_s]
        parents: List[int] = [-1]

        for _ in range(max_iter):
            # Goal biasing
            if self.rng.random() < self.goal_bias:
                q_rand = q_g.copy()
            else:
                q_rand = self.rng.uniform(self.q_min, self.q_max)

            # Nearest neighbor
            distances = [np.linalg.norm(q_rand - n) for n in nodes]
            nearest_idx = int(np.argmin(distances))
            q_near = nodes[nearest_idx]

            # Step towards q_rand
            diff = q_rand - q_near
            dist = np.linalg.norm(diff)
            if dist < 1e-6:
                continue

            step = min(self.step_size, dist)
            q_new = q_near + (diff / dist) * step

            # Clamp to joint limits
            q_new = np.clip(q_new, self.q_min, self.q_max)

            # Collision check
            if self.is_segment_free(q_near, q_new):
                nodes.append(q_new)
                parents.append(nearest_idx)

                # Check if reached goal region
                if np.linalg.norm(q_new - q_g) <= self.step_size:
                    if self.is_segment_free(q_new, q_g):
                        nodes.append(q_g)
                        parents.append(len(nodes) - 2)

                        # Reconstruct path
                        path = []
                        curr = len(nodes) - 1
                        while curr != -1:
                            path.append(nodes[curr])
                            curr = parents[curr]
                        path.reverse()
                        return self.shortcut_smoothing(path)

        return None

    def shortcut_smoothing(self, path: List[np.ndarray], iterations: int = 20) -> List[np.ndarray]:
        """Post-process path by shortcutting redundant intermediate waypoints."""
        if len(path) <= 2:
            return path

        smoothed = list(path)
        for _ in range(iterations):
            if len(smoothed) <= 2:
                break
            idx1 = self.rng.integers(0, len(smoothed) - 2)
            idx2 = self.rng.integers(idx1 + 2, len(smoothed))
            if self.is_segment_free(smoothed[idx1], smoothed[idx2]):
                smoothed = smoothed[:idx1 + 1] + smoothed[idx2:]

        return smoothed


def main():
    print("=" * 65)
    print("Lesson 22: C-Space RRT Trajectory Planner & Obstacle Avoidance")
    print("=" * 65)

    q_min = np.full(6, -np.pi)
    q_max = np.full(6, np.pi)
    planner = CSpaceRRTPlanner(q_min, q_max, step_size_rad=0.2, seed=10)

    # Add virtual C-space obstacle between start and goal
    # Obstacle on Joint 2 and Joint 3
    obs_low = np.array([-np.pi, 0.2, -0.5, -np.pi, -np.pi, -np.pi])
    obs_high = np.array([np.pi, 0.8, 0.5, np.pi, np.pi, np.pi])
    planner.add_obstacle_box(obs_low, obs_high)

    q_start = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    q_goal = np.array([0.5, 1.2, 0.8, 0.0, 0.0, 0.0])

    path = planner.plan(q_start, q_goal, max_iter=2000)

    if path:
        print(f"\nPath Successfully Planned! Number of Waypoints: {len(path)}")
        print(f"  Start: {np.round(path[0], 2).tolist()} rad")
        print(f"  Goal:  {np.round(path[-1], 2).tolist()} rad")
    else:
        print("\nFailed to find path.")


if __name__ == "__main__":
    main()
