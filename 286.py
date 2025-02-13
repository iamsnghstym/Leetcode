from collections import deque

class Pair:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        return 0 <= row < rows and 0 <= col < cols

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # Get all treasure chests
                if grid[row][col] == 0:
                    q.append(Pair(row, col, 0))
                    visited[row][col] = True

        # Do BFS
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            pair = q.popleft()
            row, col, dist = pair.row, pair.col, pair.dist
            for dir in dirs:
                nrow, ncol = row + dir[0], col + dir[1]
                if self.isValid(grid, nrow, ncol) and grid[nrow][ncol] != -1 and not visited[nrow][ncol]:
                    grid[nrow][ncol] = dist+1
                    q.append(Pair(nrow, ncol, dist+1))
                    visited[nrow][ncol] = True