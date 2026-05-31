class Solution:
    def isAnagram(self, s: str, t: str) -> bool:



        '''
        anagram: str that contains the exact same chars as another str, ordering can differ

        s: str, t: str

        s and t consist of lowercase English letters.
        '''

        if len(s) != len(t):
            return False

        seen_chars = [0] * 26

        # 'a' - [1, 0, ...]


        for s_char in s:
            seen_chars[ord(s_char) - ord('a')] += 1


        for t_char in t:

            if seen_chars[ord(t_char) - ord('a')] == 0:
                return False
            
            seen_chars[ord(t_char) - ord('a')] -= 1


        return sum(seen_chars) == 0
        

        




        

