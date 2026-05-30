class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        RED = 0
        WHITE = 1
        BLUE = 2


        r_count = 0
        w_count = 0
        b_count = 0
        

        for num in nums:
            if num == RED:
                r_count += 1

            if num == WHITE:
                w_count += 1

            if num == BLUE:
                b_count += 1

        
        for i in range(len(nums)):
            if i < r_count:
                nums[i] = RED
                continue
            if i < r_count + w_count:
                nums[i] = WHITE
                continue
            
            nums[i] = BLUE


        return 