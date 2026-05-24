class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        solution = 0 #worst case scenario

        # naive solution:
        # for each day, look at all days in future and see profit

        # as we step through the days, we see if there is a max profit

        min_price = prices[0] # we know prices is not empty
        for p in prices:

            min_price = min(min_price, p)

            solution = max(p - min_price, solution)




        return solution
        