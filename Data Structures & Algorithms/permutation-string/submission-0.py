class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        k = len(s1)

        for i, c in enumerate(s2):
            window[ord(c) - ord('a')] += 1

            if i >= k:
                left = s2[i - k]
                window[ord(left) - ord('a')] -= 1

            if window == need:
                return True

        return False
