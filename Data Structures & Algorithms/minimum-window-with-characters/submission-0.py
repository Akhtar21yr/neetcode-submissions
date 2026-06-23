class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0

        min_len = float("inf")
        res_left = 0
        res_right = 0

        for right in range(len(s)):

            # Add current character to window
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Check if this character requirement is satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Window is valid
            while have == need_count:

                # Update shortest answer
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    res_left = left
                    res_right = right

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # If requirement breaks, reduce have
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[res_left:res_right + 1]