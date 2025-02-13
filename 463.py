class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        return True if row >=0  and col >= 0 and row < rows and col < cols else False

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        perimeter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    perimeter = self.dfs(row, col, grid, visited)
        return perimeter

    def dfs(self, row: int, col: int, grid: List[list[int]], visited: List[List[bool]]) -> int:
        visited[row][col] = True
        perimeter = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in dirs:
            nrow, ncol = row + dr, col + dc
            if not self.isValid(grid, nrow, ncol) or grid[nrow][ncol] == 0:
                perimeter += 1
            elif grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                perimeter += self.dfs(nrow, ncol, grid, visited)
        return perimeter