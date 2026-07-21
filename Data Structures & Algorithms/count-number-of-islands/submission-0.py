class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))

            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if valid_position(new_row, new_col):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col)) 

        def valid_position(r, c):
            if (r, c) in visited:
                return False

            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == "1":
                return True

            return False


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(visited)
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands
