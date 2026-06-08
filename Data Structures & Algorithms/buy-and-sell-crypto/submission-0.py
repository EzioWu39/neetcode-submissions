class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        ans = 0
        for price in prices:
            ans = max(ans, max(0, price - lowest))
            lowest = min(lowest, price)
        return ans