class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        count = len(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
                
            else:
                count -= 1

        print(count)

        return count


        