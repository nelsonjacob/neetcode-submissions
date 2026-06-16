
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        V = defaultdict(list)
        for ai, bi in trust:
            V[ai].append(bi)


        judge_candidate = None
        for person in range(1, n+1):
            if person not in V:
                judge_candidate = person

        for person in range(1, n+1):

            if person == judge_candidate:
                continue
            
            if judge_candidate not in V[person]:
                return -1
        
        return judge_candidate