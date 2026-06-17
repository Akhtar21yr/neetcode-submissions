class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copyele = heights.copy()
        copyele.sort()
        count = 0

        for i in range(len(heights)):
            if heights[i] != copyele[i]:
                count += 1


        return count
        