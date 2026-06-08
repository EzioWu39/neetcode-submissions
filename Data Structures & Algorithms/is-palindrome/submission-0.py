class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        mid = len(s)//2 if len(s) % 2 == 0 else len(s)//2 + 1
        second = s[mid:][::-1]
        for i in range(len(second)):
            if s[i].lower() != second[i].lower():
                return False
        return True