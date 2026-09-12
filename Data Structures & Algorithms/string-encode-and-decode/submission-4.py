class Solution:


    def encode(self, strs: List[str]) -> str:
        encode_list = list()

        for s in strs:
            encode_list.append(str(len(s)))
            encode_list.append('|')
            encode_list.append(s)

        return "".join(encode_list)

    def decode(self, s: str) -> List[str]:

        decoded_list = list()

        start_len_offset = 0
        i = 0

        while i < len(s):
            if s[i] != '|':
                i += 1
                continue
            

            str_len = int(s[start_len_offset:i])
            decoded_list.append(s[i+1: i+1+str_len])

            start_len_offset = i+1+str_len
            i = start_len_offset
        

        return decoded_list


        


