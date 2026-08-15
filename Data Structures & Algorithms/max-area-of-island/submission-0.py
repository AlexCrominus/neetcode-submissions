class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r:int,c:int) -> int:
            nonlocal visited
            ROWS, COLS = len(grid), len(grid[0])
            if min(r,c) < 0 or (r,c) in visited or r == ROWS or c == COLS or grid[r][c] == 0:         
                return 0

            visited.add((r,c))
            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        visited = set()
        maxArea = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1  and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea  