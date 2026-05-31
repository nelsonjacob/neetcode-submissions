class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        max_water = 0

        low, high = 0, len(heights) - 1

        while low < high:


            height = high - low

            max_water = max(max_water, height * min(heights[low], heights[high]))

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1

        return max_water