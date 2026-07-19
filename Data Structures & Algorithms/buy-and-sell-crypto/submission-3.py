class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_p = float('inf')
        max_diff = 0
        for p in prices:
            min_p = min(min_p, p)
            max_diff = max(max_diff, p - min_p)
        return max_diff
