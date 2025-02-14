from typing import List
from collections import deque

class Pair:
    def __init__(self, row, col, time):
        self.row = row
        self.col = col
        self.time = time

class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        q = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    visited[row][col] = True
                    q.append(Pair(row, col, 0))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        timeToRot = 0
        while q:
            pair = q.popleft()
            row, col, time = pair.row, pair.col, pair.time
            timeToRot = max(timeToRot, time)

            for dir in dirs:
                nrow, ncol = row + dir[0], col + dir[1]
                if self.isValid(grid, nrow, ncol) and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
                    visited[nrow][ncol] = True
                    q.append(Pair(nrow, ncol, time+1))
                    fresh -= 1

        return timeToRot if fresh == 0 else -1
