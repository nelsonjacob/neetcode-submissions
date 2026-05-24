class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        dp = [None] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0

        def backtrack(i):

            if dp[i] is not None:
                return dp[i]


            dp[i] = min(backtrack(i-1)+cost[i-1], backtrack(i-2)+cost[i-2])
            return dp[i]

        return backtrack(len(cost))

            
            
            


        