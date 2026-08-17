class Solution:
    def trap(self, height: List[int]) -> int:

        max_water = [0] * len(height)


        max_el = 0
        for i, h in enumerate(height):
            max_el = max(max_el, h)

            max_water[i] = max_el


        max_suffix_height = 0


        water_total = 0 
        for i in range(len(height) - 1, -1, -1):
            max_suffix_height = max(max_suffix_height, height[i])
            water_total += min(max_water[i], max_suffix_height) - height[i]

        return water_total




                