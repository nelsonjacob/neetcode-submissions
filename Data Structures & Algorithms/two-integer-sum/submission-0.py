class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_dict = dict()

        for i, num in enumerate(nums):

            k = target - num

            if k in seen_dict:
                return [seen_dict[k], i]

            seen_dict[num] = i


        # we shouldn't reach here
        return []        