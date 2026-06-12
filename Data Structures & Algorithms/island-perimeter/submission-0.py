class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # land can have [0,4 coastlines]
        
        LAND = 1
        WATER = 0
        neighbors = [(1,0), (-1, 0), (0,1), (0, -1)]


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    
                    
                    for r1, c1 in neighbors:
                        neighbor_row = r + r1
                        neighbor_col = c + c1

                        if neighbor_row < 0 or neighbor_row >= rows or neighbor_col < 0 or neighbor_col >= cols or grid[neighbor_row][neighbor_col] == WATER:
                            perimeter += 1

        return perimeter
        