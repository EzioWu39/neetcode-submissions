class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                while stack and temp > stack[-1][1]:
                    pre_index, _ = stack.pop()
                    ans[pre_index] = i - pre_index
                stack.append((i, temp))
        return ans