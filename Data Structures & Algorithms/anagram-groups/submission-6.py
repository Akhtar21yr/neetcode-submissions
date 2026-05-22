class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _pair = {}

        for i in strs:
            count = [0]*26

            for j in i :
                count[ord(j)-ord('a')] += 1
            
            _pair[tuple(count)] = _pair.get(tuple(count),[]) 
            _pair[tuple(count)].append(i)

        return list(_pair.values())
        