
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        '''
        Fun problem! 'canonical coin set' is one that can be solved with greedy algo
        For example, US system of [0.01, 0.05, 0.1, 0.25, 1]
        '''

        dp = dict()
        dp[amount] = 0
        queue = deque([amount])

        
        while queue:
            current_amount = queue.popleft()
            
            if current_amount == 0: 
                return dp[0]
            for coin in coins:
                new_amount = current_amount - coin
                if new_amount in dp or new_amount < 0:
                    continue
                
                dp[new_amount] = dp[current_amount]+1
                queue.append(new_amount)
        
        return -1



        





