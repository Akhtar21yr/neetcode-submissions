class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in _dict :
                return [_dict[val],i]
            else :
                _dict[nums[i]] = i
        