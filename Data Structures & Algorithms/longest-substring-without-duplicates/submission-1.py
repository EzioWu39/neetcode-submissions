class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = ans = 0

        for r, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c] + 1)

            seen[c] = r
            ans = max(ans, r - l + 1)

        return ans