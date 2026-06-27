class Solution:
    def isValid(self, s: str) -> bool:
        hash = {'(':')','[':']','{':'}'}
        stack = []

        if len(s) <= 1:
            return False

        for para in s:
            if para in hash:
                stack.append(hash[para])
                continue

            if not stack:
                return False

            if stack and stack.pop() != para:
                return False

            




        return not stack

            

        