
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:



        votes_in = [0] * (n+1)
        votes_out = [0] * (n+1)


        for a, b in trust:
            votes_out[a] += 1
            votes_in[b] += 1
        

        for person in range(1,n+1):
            if votes_out[person] == 0 and votes_in[person] == n-1:
                return person
        

        return -1
