from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_window = ""
        
        t_counter = Counter(t)

        keys = len(t_counter)
        valid_keys = 0
        s_counter = defaultdict(int)

        
        p_ahead, p_follow = 0, 0

        while p_ahead < len(s):

            c_ahead = s[p_ahead]
            if c_ahead not in t_counter:
                p_ahead += 1
                continue
            
            s_counter[c_ahead] += 1

            if s_counter[c_ahead] == t_counter[c_ahead]:
                valid_keys += 1

            while keys == valid_keys:

                c_follow = s[p_follow]

                while c_follow not in t_counter:
                    p_follow += 1
                    c_follow = s[p_follow]
                
                if not min_window or len(s[p_follow:p_ahead+1]) < len(min_window):
                    min_window = s[p_follow:p_ahead+1]
                
                if s_counter[c_follow] == t_counter[c_follow]:
                    valid_keys -= 1

                s_counter[c_follow] -= 1
                p_follow += 1

            p_ahead += 1

        return min_window
        