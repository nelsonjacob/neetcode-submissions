class Solution:
    def maxScore(self, s: str) -> int:
        

        n = len(s)

        score = [0] * n
        one_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                one_count += 1
            score[i] = one_count
            

        zero_count = 0
        max_score = 0

        for i in range(n - 1):
            if s[i] == '0':
                zero_count += 1
            score[i] = zero_count
            max_score = max(max_score, score[i] + score[i + 1])

        return max_score