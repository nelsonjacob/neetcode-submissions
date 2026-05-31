class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        We need to find the max water stored in possible containers

        Input: heights: List[int]

        2 <= height.length <= 1000
        0 <= height[i] <= 1000

        Not super concerned about negative heights, nor invalid list input



        How do we find the area the container can hold:

        [1, 2, 3]

        What is the area we can hold for [1,3]

        index(high) - index(low) * min(high, low)


        '''


        max_water = 0



        # for i in range(len(heights)):
        #     for j in range(len(heights)):

        #         max_water = max(max_water, (j-i) * min(heights[i], heights[j]))

        low, high = 0, len(heights) - 1

        while low < high:

            max_water = max(max_water, (high - low) * min(heights[high], heights[low]))

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1








        return max_water