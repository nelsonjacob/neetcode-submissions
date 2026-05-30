class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        n = len(nums)

        solution = [0] * (n * 2)
        for i, num in enumerate(nums):
            solution[i] = num
            solution[i + n] = num

        return solution        