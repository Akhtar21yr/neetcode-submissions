class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in s_dict :
                s_dict[sorted_s].append(s)
            else :
                s_dict[sorted_s] = [s]

        return list(s_dict.values())