class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue

            count = 0

            while num + count in nums:
                count+= 1

            lcs = max(lcs,count)

        return lcs

            
        