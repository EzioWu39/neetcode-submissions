class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        count = Counter()
        left = 0
        ans = 0
        max_feq = 0

        for right, char in enumerate(s):
            count[char] += 1
            max_feq = max(max_feq, count[char])

            while (right - left + 1) - max_feq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans