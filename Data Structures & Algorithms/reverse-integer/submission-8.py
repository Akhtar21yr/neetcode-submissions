class Solution:
    def reverse(self, x1: int) -> int:
        if x1 is 0 :
            return 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        x = abs(x1)
        res = 0
        while x > 0 :
            n = x%10
            res = n + res * 10
            x = x//10

        return res*(x1//abs(x1)) if INT_MIN < res < INT_MAX else 0