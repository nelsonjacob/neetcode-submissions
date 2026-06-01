class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        paren_map = {']':'[','}':'{',')':'('}

        for c in s:

            if c not in paren_map.keys():
                stack.append(c)
                continue
            

            if not stack or stack.pop() != paren_map[c]:
                return False

        

        return len(stack) == 0
