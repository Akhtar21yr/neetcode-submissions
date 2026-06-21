class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = maxfreq = maxwindow = 0
        _map ={}

        while right < len(s):
            _map[s[right]] = _map.get(s[right],0) + 1
            maxfreq = max(maxfreq,_map[s[right]])

            while (right - left+1) - maxfreq > k:
                left += 1
                _map[s[left -1]] -= 1

            maxwindow = max(maxwindow,right-left+1)
            right += 1

        return maxwindow
        