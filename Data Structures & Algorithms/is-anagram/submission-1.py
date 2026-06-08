class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        chars_s = [0] * 26
        chars_t = [0] * 26
        for char in s:
            chars_s[ord(char) - ord("a")] += 1
        for char in t:
            chars_t[ord(char) - ord("a")] += 1
        
        return chars_s == chars_t