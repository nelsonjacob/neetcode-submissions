class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        

        k_needed = tickets[k]
        time_needed = 0
        for i, el in enumerate(tickets):
            time_needed += min(k_needed, el) if i <= k else min(k_needed - 1, el) 


        return time_needed