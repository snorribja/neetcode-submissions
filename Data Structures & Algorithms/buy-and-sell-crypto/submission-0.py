class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        st = 0
        max_profit = 0
        for p1 in prices[:-1]:
            st += 1
            for j in range(st, n):
                profit = prices[j] - p1
                max_profit  = max(profit, max_profit)
        return max_profit   

