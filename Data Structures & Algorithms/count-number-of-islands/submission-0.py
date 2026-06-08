class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y) -> None:
            if x < 0 \
            or y < 0 \
            or x >= len(grid) \
            or y >= len(grid[0]) \
            or grid[x][y] == "0":
                return
            
            grid[x][y] = "0"

            dirction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for dir_x, dir_y in dirction:
                dfs(x + dir_x, y + dir_y)
        ans = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    ans += 1
                    dfs(x, y)
        return ans
            