class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        num_val = 0

        for i, num in enumerate(nums):

            if num == val:
                num_val += 1
                continue


            nums[i - num_val] = num


        return len(nums) - num_val        