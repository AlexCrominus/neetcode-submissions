from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Add all initially rotten oranges to the queue
        # and count fresh oranges.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        minutes = 0

        while queue and fresh > 0:
            # Everything currently in the queue spreads
            # during the same minute.
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes