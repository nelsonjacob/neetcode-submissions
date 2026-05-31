class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = dict()

        def get_anagram_hash(s):
            '''
            take any string, and return a key that is deterministic for any anagram that is the same
            
            
            Intuition: not the exact approach
            'ab' -> 'a-b'
            'ba' -> 'a-b'
            '''

            freq_array = [0] * 26

            for s_char in s:
                freq_array[ord(s_char) - ord('a')] += 1
            
            return "-".join(str(freq_array))






        for str_a in strs:

            anagram_hash = get_anagram_hash(str_a)

            if anagram_hash in anagram_map:
                anagram_map[anagram_hash].append(str_a)
            else: 
                anagram_map[anagram_hash] = [str_a]
            

        return list(anagram_map.values())



        