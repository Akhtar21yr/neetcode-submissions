class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amnt = 0
        n = len(heights)

        for i in range(n):
            for j in range(i+1,n):
                min_height = min(heights[i],heights[j])

                water_contain = min_height * (j-i)

                max_amnt = max(max_amnt,water_contain)

        return max_amnt
        