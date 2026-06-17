class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for i in arr:
            count[i] = count.get(i,0) + 1

        maxl = -1

        for i,j in count.items():
            if i == j:
                maxl  =max(maxl,i)

        return      maxl  