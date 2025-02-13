class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        return True if row >=0  and col >= 0 and row < rows and col < cols else False

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    received_area = self.dfs(row, col, grid, visited)
                    area = max(area, received_area)
        return area

    def dfs(self, row: int, col: int, grid: List[list[int]], visited: List[List[bool]]) -> int:
        visited[row][col] = True
        area = 1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in dirs:
            nrow, ncol = row + dr, col + dc
            if self.isValid(grid, nrow, ncol) and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                area += self.dfs(nrow, ncol, grid, visited)
        return area