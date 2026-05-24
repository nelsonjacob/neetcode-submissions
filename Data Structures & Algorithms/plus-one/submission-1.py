class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        l = digits[::-1] # [1,2,3,4] -> [4,3,2,1]

        # case 0: if we are adding 1 to any number in the range 0-8, we just add it

        # case 1: else, we have a carry

        iter = 0
        carry = False

        while (iter < len(l)):
            if l[iter] >= 0 and l[iter] < 9:
                l[iter] += 1
                carry = False
                break
            else:
                l[iter] = 0
                carry = True
            
            iter += 1
            
        
        if carry:
            l.append(1)

        return l[::-1]

        



        