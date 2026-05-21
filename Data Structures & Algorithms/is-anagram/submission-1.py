class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = {}
        tc = {}    

        for i in range(len(s)) :
            if s[i] in sc:
                sc[s[i]] += 1
            else :
                sc[s[i]] = 1

            if t[i] in tc :
                tc[t[i]] += 1
            else :
                tc[t[i]] = 1

                

        for i in sc :
            if i not in tc or sc[i] != tc[i]:
                return False

        return True



        