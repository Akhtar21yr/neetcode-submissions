class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        _map = {}
        windowsize = maxwindow = left = right = maxfreq = 0

        while right < len(s):
            windowsize = right - left + 1
            _map[s[right]] = _map.get(s[right],0) + 1
            maxfreq = max(maxfreq,_map[s[right]])

            ch2change = windowsize - maxfreq

            if ch2change > k :
                left += 1
                _map[s[left-1]] -= 1
                maxwindow = max(maxwindow,windowsize-1)
            else:
                maxwindow = max(maxwindow,windowsize)

            right += 1

        
            
        






        return maxwindow
        