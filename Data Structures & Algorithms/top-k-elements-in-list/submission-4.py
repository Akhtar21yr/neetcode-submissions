class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for i in nums :
            counter[i] = counter.get(i,0) + 1

        freq= [[] for _ in range(len(nums))]
        print(freq)

        for i,j in counter.items():
            freq[j-1].append(i)

        res = []


        for i in freq[::-1]:
            for j in i :
                res.append(j)
                if len(res) == k :
                    return res
        