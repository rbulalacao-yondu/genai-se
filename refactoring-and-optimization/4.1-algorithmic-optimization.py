"""
pairwise_naive.py
-----------------
Compute all pair‑wise Euclidean distances with a **double for‑loop**.
Designed to be slow enough that /optimize → “use KDTree” shows a dramatic
speed‑up in Copilot’s diff and the timing printout.
"""

import math
import random
import time
from typing import List, Tuple

Point = Tuple[float, float]

def generate_points(n: int, seed: int = 42) -> List[Point]:
    """Return `n` random 2‑D points in the unit square."""
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def pairwise_distances(points: List[Point]) -> List[List[float]]:
    """
    Naïve O(n²) pair‑wise distance matrix.

    *No numpy—pure Python to keep it deliberately slow.*  
    """
    n = len(points)
    dist = [[0.0] * n for _ in range(n)]

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            d = math.hypot(x2 - x1, y2 - y1)
            dist[i][j] = dist[j][i] = d
    return dist


if __name__ == "__main__":
    NUM_POINTS = 5_000       # tweak to taste—10 000 is “coffee break” slow
    pts = generate_points(NUM_POINTS)

    t0 = time.perf_counter()
    _ = pairwise_distances(pts)
    elapsed = time.perf_counter() - t0

    print(f"Computed {NUM_POINTS}² distances in {elapsed:.2f} s")
