class Solution:
    def isPalindrome(self, s: str) -> bool:
        refPal = ''
        for i in s :
            if i.isnumeric() or i.isalpha():
                refPal += i.lower()

        return refPal == refPal[::-1]
        