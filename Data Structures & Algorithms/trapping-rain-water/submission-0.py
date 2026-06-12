class Solution:
    def trap(self, height: List[int]) -> int:
        _sum = 0
        n = len(height)

        for i in range(1,n-1):
            left_max = 0
            for k in range(i):
                left_max = max(left_max,height[k])

            right_max = 0
            for k in range(i+1,n):
                right_max = max(right_max,height[k])



            _sum += max(min(left_max,right_max) - height[i],0)

        return _sum

        