class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            
            if n in seen:
                return False

            seen.add(n)

            _sum = 0

            while n >0:
                temp = n%10
                _sum += temp **2
                n //= 10
            n = _sum 

        return True
