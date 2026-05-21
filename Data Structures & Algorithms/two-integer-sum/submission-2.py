class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {nums[i] :i for i in range(len(nums)) }

        


        for i in range(len(nums)):
            diff = target - nums[i] 

            if diff in dic and dic[diff] != i :
                return [i,dic[diff]]


        