class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        copyn = abs(n)
        while copyn>0:
            res *= x
            copyn -= 1
        
        return res if n > 0 else 1/res