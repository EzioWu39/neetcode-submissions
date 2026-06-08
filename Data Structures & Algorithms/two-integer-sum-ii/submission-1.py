class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict

        seen = defaultdict(int)
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target-num], i + 1]
            seen[num] = i + 1
        return []