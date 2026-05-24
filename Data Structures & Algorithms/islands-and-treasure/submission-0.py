from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return grid

        rows, cols = len(grid), len(grid[0])

        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row+1, col))
                    queue.append((row-1, col))
                    queue.append((row, col+1))
                    queue.append((row, col-1))

        
        if not queue:
            return grid

        
        current_distance = 1
        continue_traversal = True

        while continue_traversal:

            continue_traversal = False
            
            for _ in range(len(queue)):

                row, col = queue.popleft()
                if (row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 2147483647):
                    continue

                grid[row][col] = current_distance

                queue.append((row+1, col))
                queue.append((row-1, col))
                queue.append((row, col+1))
                queue.append((row, col-1))

                continue_traversal = True

            current_distance += 1  


        return         









        