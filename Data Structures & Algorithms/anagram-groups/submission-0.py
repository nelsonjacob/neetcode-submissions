class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ag_dict = dict()
        for st in strs:
            sorted_st = tuple(sorted(st))
            if sorted_st in ag_dict:
                ag_dict[sorted_st].append(st)
            else:
                ag_dict[sorted_st] = [st]
        
        return list(ag_dict.values())
            

        