class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxlen = left = right = 0

        while right < len(s):
            if s[right] in seen:
                maxlen = max(maxlen,right - left)
                seen.remove(s[left])
                left += 1

            else:
                seen.add(s[right])
                right += 1

        else:
            maxlen = max(maxlen,right-left)
        return maxlen