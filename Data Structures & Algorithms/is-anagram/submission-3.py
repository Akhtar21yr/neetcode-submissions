class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        _counter = {}

        for i in range(len(s)):
            _counter[s[i]] = _counter.get(s[i],0) + 1
            _counter[t[i]] = _counter.get(t[i],0) - 1


        for key,value in _counter.items():
            if value != 0:
                return False

        return True
        