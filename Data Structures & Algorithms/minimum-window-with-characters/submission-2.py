class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for i in t:
            freq_t[i] = freq_t.get(i,0) + 1

        left = right = best_left = best_right = have = 0
        min_len = float('inf')
        window_freq = {}
        need = len(freq_t)

        while right < len(s):
            window_freq[s[right]] = window_freq.get(s[right],0)+1

            if s[right] in freq_t and window_freq[s[right]] == freq_t[s[right]] :
                have += 1

            while have == need:
                window = right - left + 1

                if min_len > window:
                    min_len = window 
                    best_left = left
                    best_right = right 

                window_freq[s[left]] -= 1

                if s[left] in freq_t and window_freq[s[left]] < freq_t[s[left]]:
                    have -= 1

                left += 1

            right += 1

        if min_len == float('inf'):
            return ""

        return s[best_left:best_right+1]
        