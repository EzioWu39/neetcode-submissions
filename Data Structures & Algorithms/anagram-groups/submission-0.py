class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            feq = [0] * 26
            for c in s:
                feq[ord(c) - ord('a')] += 1
            feq = "".join(str(feq))
            ans[feq].append(s)
        return list(ans.values())