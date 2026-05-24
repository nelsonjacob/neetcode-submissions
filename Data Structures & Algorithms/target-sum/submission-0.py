class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        total_sum_ways = 0


        def dfs(index, total):

            nonlocal total_sum_ways

            if index == len(nums):
                if target == total:
                    total_sum_ways += 1
                return
            
            dfs(index+1, total+nums[index])
            dfs(index+1, total-nums[index])

            return

            
        dfs(0, total_sum_ways)

        return total_sum_ways


                

        