class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        k = 0

        for i in nums:
            if i-1 in nums:
                continue
            
            large = 1
            while i+1 in nums:
                large += 1
                i += 1

            k = max(large,k)



        return k