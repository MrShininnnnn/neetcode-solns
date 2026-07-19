class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i, a in enumerate(prices):
            for j, b in enumerate(prices):
                if i < j:
                    max_p = max(max_p, b - a)
        return max_p
