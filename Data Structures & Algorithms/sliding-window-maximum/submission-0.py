from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            # Remove indices that are outside the window
            if dq[0] < right - k + 1:
                dq.popleft()

            # Window is complete
            if right >= k - 1:
                res.append(nums[dq[0]])

        return res