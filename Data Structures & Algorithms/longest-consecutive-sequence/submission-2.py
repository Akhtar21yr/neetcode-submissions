class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0

        for i in range(len(nums)):
            if nums[i] - 1 in nums:
                continue
            count = 0
            while nums[i] + count in nums:
                count += 1

            lcs = max(lcs,count)

        return lcs

            
        