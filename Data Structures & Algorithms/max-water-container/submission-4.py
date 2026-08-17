class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        max_water = 0

        low, high = 0, len(heights) - 1

        while low < high:


            low_height, high_height = heights[low], heights[high]
            max_water = max(max_water, min(low_height, high_height) * (high - low))

            if low_height < high_height:
                low += 1 
            else:
                high -= 1

        return max_water