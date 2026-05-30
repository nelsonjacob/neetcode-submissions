class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        majority_so_far = nums[0]
        majority_count = 1

        for i in range(1, len(nums)):
            
            if majority_count == 0:
                # elect a new leader
                majority_so_far = nums[i]
                majority_count += 1
                continue
            
            if nums[i] == majority_so_far:
                majority_count += 1
                continue

            majority_count -= 1
    
        return majority_so_far
            




        