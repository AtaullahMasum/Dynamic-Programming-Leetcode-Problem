class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - min_buy
            maxProfit = max(maxProfit, profit)
            min_buy = min(min_buy, prices[i])
        return maxProfit