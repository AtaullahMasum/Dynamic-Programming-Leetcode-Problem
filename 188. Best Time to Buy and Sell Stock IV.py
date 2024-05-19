# These question as presious stock questions 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0]*(k+1) for _ in range(2)]
        curr = [[0]*(k+1) for _ in range(2)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy:
                        curr[buy][cap] = max (-prices[i] + ahead[0][cap], 0+ ahead[1][cap])
                    else:
                        curr[buy][cap] = max(prices[i] + ahead[1][cap-1], 0+ ahead[0][cap])
                ahead = curr
        return ahead[1][k]