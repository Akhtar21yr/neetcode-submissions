class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        _sum = {}

        for i in range(len(nums)):
            val = target - nums[i]

            if val in _sum:
                return [_sum[val],i]

            _sum[nums[i]] = i
        