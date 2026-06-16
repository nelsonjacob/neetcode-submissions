class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        LAND = 1
        WATER = 0


        neighbors = [(1,0), (-1,0), (0,1), (0, -1)]
        max_island_area = 0

        def get_island_area(row, col):
        
            island_size = 1
            grid[row][col] = WATER

            for r1, c1 in neighbors:

                new_row, new_col = row+r1, col+c1

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == LAND:
                    island_size = island_size + get_island_area(new_row, new_col)
                    
            return island_size

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND:
                    max_island_area = max(max_island_area, get_island_area(row, col))



        return max_island_area
        