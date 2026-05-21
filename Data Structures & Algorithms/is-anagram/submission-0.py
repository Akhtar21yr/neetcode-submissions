class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = {}
        tc = {}    

        for i in s :
            if i in sc:
                sc[i] += 1
            else :
                sc[i] = 1

        for i in t :
            if i in tc :
                tc[i] += 1
            else :
                tc[i] = 1

        for i in sc :
            if i not in tc or sc[i] != tc[i]:
                return False

        return True



        