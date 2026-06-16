class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0

        for word in words:
            valid = True
            for ch in word:
                if ch not in allowed:
                    valid = False

            if valid:
                count += 1

        return count
        