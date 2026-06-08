class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)

        ans = ""
        left = 0

        for right, c in enumerate(s):
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans):
                    ans = curr

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return ans