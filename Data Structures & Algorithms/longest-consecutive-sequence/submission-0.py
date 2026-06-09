class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i =0 
        k = 0

        while i < len(nums):
            count = 1
            ele = nums[i]
            while ele + 1 in nums:
                ele += 1
                count += 1

            if count > k :
                k = count 

            i += 1


        return k