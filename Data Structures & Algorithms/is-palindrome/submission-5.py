class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_el = 0
        end_el = len(s) - 1
        while start_el < end_el:
            # check 1: s[start_el] is a alphanumeric char
            if not s[start_el].isalnum():
                start_el += 1
                continue
            if not s[end_el].isalnum():
                end_el -= 1
                continue
            if s[start_el].lower() != s[end_el].lower():
                return False
            start_el += 1
            end_el -= 1
        return True