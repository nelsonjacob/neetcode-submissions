class Solution:
    def isAnagram(self, s: str, t: str) -> bool:



        '''
        anagram: str that contains the exact same chars as another str, ordering can differ

        s: str, t: str

        s and t consist of lowercase English letters.
        '''


        if len(s) != len(t):
            return False
        

        counts = [0] * 26

        for s_char in s:
            counts[ord(s_char) - ord('a')] += 1
        

        for t_char in t:
            counts[ord(t_char) - ord('a')] -= 1

            if counts[ord(t_char) - ord('a')] < 0:
                return False
        

        return True


        
        
