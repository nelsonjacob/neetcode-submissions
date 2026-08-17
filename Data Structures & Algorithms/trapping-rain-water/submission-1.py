class Solution:
    def trap(self, height: List[int]) -> int:
        
        water_total = 0


        low, high = 0, len(height) - 1
        max_low, max_high = height[0], height[len(height) - 1]

        while low < high:


            if max_low < max_high:
                low += 1
                max_low = max(max_low, height[low])
                water_total += max_low - height[low]
            else:
                high -= 1
                max_high = max(max_high, height[high])
                water_total += max_high - height[high]

        return water_total





                