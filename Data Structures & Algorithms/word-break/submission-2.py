class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        max_len_word = max([len(word) for word in wordDict])
        wordSet = set(wordDict)
        
        
        def recurse(index):

            if index >= len(s):
                return True
            if s[index:] in memo:
                return memo[s[index:]]
        
        
            for upperBound in range(index, min(index + max_len_word, len(s)) + 1):
                if s[index:upperBound] in wordSet and recurse(upperBound):
                    memo[s[index:]] = True
                    return True
                
            memo[s[index:]] = False
            return False
        
            
        return recurse(0)
        
        