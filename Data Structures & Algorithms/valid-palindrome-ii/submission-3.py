class Solution:
    
    

    def isValidSubPalindrome(self, s: str) -> bool:


        front, back = 0, len(s) - 1

        while front < back:
            

            if s[front] != s[back]:
                return False

            front += 1
            back -= 1
        
        return True


    
    def validPalindrome(self, s: str) -> bool:


        front, back = 0, len(s) - 1



        while front < back:
            

            if s[front] != s[back]:
                return self.isValidSubPalindrome(s[front+1:back+1]) or self.isValidSubPalindrome(s[front:back])

            front += 1
            back -= 1
        
        return True



