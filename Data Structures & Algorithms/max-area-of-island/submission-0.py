class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y) -> int:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) \
                or grid[x][y] == 0:
                    return 0
            grid[x][y] = 0
            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            sums = 0
            for dir_x, dir_y in direction:
                sums += dfs(x + dir_x, y + dir_y)
            return 1 + sums
        ans = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    area = dfs(x, y)
                    ans = max(ans, area)
        return ans