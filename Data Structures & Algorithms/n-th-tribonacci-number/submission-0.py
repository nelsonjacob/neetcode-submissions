class Solution:
    def tribonacci(self, n: int) -> int:


        tn = 0
        tn_plus1 = 1
        tn_plus2 = 1

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        for _ in range(2,n):

            t_curr = tn + tn_plus1 + tn_plus2

            tn = tn_plus1
            tn_plus1 = tn_plus2
            tn_plus2 = t_curr


        return tn_plus2