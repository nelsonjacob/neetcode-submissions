class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Time vs space approach

        #Consider the inputs, if each is unique, not duplicate, then a set, will be the same length

        return len(set(nums))!=len(nums)
         