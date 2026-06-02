class Solution:
    def search(self, nums: List[int], target: int) -> int:


        '''
        nums: [int] (unique and sorted asc), target (int)

        Implement fn to determine existance of target in nums:

        Must run in O(log n) time)

        '''


        # for i, el in nums:
        #     if el == target:
        #         return i

        # return -1

        # Binary search algorithm:


        low, high = 0, len(nums) - 1

        
        while low <= high: # is it < or <=

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        return -1

                


        