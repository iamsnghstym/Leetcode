class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    self.markIslands(grid, row, col, visited)
        return islands

    def markIslands(self, grid: List[List[int]], row: int, col: int, visited: List[list[bool]]) -> None:
        visited[row][col] = True

        dirs = [[0, -1], (0, 1), (-1, 0), (1, 0)]
        for i in range(4):
            nrow, ncol = row + dirs[i][0], col + dirs[i][1]
            if self.isValid(grid, nrow, ncol) and not visited[nrow][ncol] and grid[nrow][ncol] == "1":
                self.markIslands(grid, nrow, ncol, visited)