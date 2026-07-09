class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        move_back = 0


        prev_seen_el = None
        for i, el in enumerate(nums):
            if el != prev_seen_el:
                prev_seen_el = el
            else:
                move_back += 1
            

            nums[i-move_back] = nums[i]
        
        return len(nums) - move_back

        