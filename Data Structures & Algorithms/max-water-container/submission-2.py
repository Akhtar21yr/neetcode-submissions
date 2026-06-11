class Solution:
    def maxArea(self, heights: List[int]) -> int:
        _max = left = 0
        right = len(heights) - 1

        while left < right:
            min_h = min(heights[left],heights[right])
            _max = max(_max,min_h*(right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1



        return _max
        