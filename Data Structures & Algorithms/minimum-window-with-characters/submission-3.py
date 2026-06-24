class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for i in t:
            freq_t[i] = freq_t.get(i,0) + 1

        left = best_left = best_right = have = 0
        need = len(freq_t)
        freq_w = {}

        min_len = float('inf')

        for right in range(len(s)):
            freq_w[s[right]] = freq_w.get(s[right],0) + 1

            if s[right] in freq_t and freq_t[s[right]] == freq_w[s[right]]:
                have += 1

            while have == need:
                window = right - left + 1
                if min_len > window :
                    min_len = window
                    best_left = left
                    best_right = right

                freq_w[s[left]] -= 1

                if s[left] in freq_t and freq_w[s[left]] < freq_t[s[left]]:
                    have -= 1

                left += 1


        if min_len == float('inf'):
            return ""

        return s[best_left:best_right+1]
        