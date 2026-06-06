from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:



        '''
        -1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

        '''



        if not grid:
            return


        
        WATER = -1
        TREASURE = 0
        INF = 2147483647
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        rows, cols = len(grid), len(grid[0])


        treasure_cells = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    treasure_cells.append((r, c))
        

        queue = deque(treasure_cells)

        current_distance = 1
        while queue:

            cells = len(queue)
            for i in range(cells):
                row, col = queue.popleft()

                for ri, ci in neighbors:
                    if 0 <= row + ri < rows and 0 <= col + ci < cols and grid[row+ri][col+ci] == INF:
                        grid[row+ri][col+ci] = current_distance
                        
                        queue.append((row + ri, col + ci))

            current_distance += 1
        
        return
                














        