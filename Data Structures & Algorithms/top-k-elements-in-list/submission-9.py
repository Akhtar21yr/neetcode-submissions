class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        _counter = {}

        for num in nums:
            _counter[num] = _counter.get(num,0) + 1

        _bucket = [0]*len(nums)

        for key, value in _counter.items():
            if _bucket[value-1] :
                _bucket[value-1].append(key)
            else :
                _bucket[value-1] = [key]

        res = []
        val = 0

        for i in _bucket[::-1]:
            if val == k or len(res)==k:
                return res

            if i :
                print('i',i)
                res.extend(i)
                val += 1

        return res

        