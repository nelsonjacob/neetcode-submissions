class Solution:
    def longestCommonPrefix(s: self, strs):
            sample_str = strs[0]
            min_len_string = min([len(el) for el in strs])

            for i in range(min_len_string):


                sample_char = sample_str[i]


                for current_str in strs:
                    if current_str[i] != sample_char:
                        return sample_str[:i]
                
            return sample_str[:min_len_string]

        