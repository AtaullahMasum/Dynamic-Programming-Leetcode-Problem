# Using Recursion Method
# Time Complexity is O(2^n)=exponentail
# Sapce Complexity is O(n)
class Solution:
    def helper(self, ind, buy, cap, prices):
        if ind== len(prices) or cap==0:
            return 0
        if buy:
            return max( -prices[ind]+ self.helper(ind+1, 0, cap, prices), 0+self.helper(ind+1, 1, cap, prices))
        return max(prices[ind] + self.helper(ind+1, 1, cap-1, prices), 0+self.helper(ind+1, 0, cap, prices))
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, 1, 2, prices)
# Using Memoization Method
# Time Complexity is O(n*2*3)
# Space Complexity is O(n*2*3) + O(n)
class Solution:
    def helper(self, ind, buy, cap, prices, dp):
        if ind== len(prices) or cap==0:
            return 0
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]
        if buy:
            dp[ind][buy][cap] = max( -prices[ind]+ self.helper(ind+1, 0, cap, prices, dp), 0+self.helper(ind+1, 1, cap, prices, dp))
            return dp[ind][buy][cap]
        dp[ind][buy][cap] = max(prices[ind] + self.helper(ind+1, 1, cap-1, prices, dp), 0+self.helper(ind+1, 0, cap, prices, dp))
        return dp[ind][buy][cap]
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1]*(3) for _ in range(2)] for _ in range(len(prices))]
        return self.helper(0, 1, 2, prices, dp)
# Using Tabulation Method
# Time Complexity is O(n*2*3)
# Sapce Complexity is O(n*2*3)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(3) for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        dp[i][buy][cap] = max (-prices[i] + dp[i+1][0][cap], 0+ dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap] = max(prices[i] + dp[i+1][1][cap-1], 0+ dp[i+1][0][cap])
        return dp[0][1][2]
# Sapce Optimization Method
# Time Complexity is O(n*2*3)
# Space Complexity is O(2*3)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0]*(3) for _ in range(2)]
        curr = [[0]*3 for _ in range(2)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        curr[buy][cap] = max (-prices[i] + ahead[0][cap], 0+ ahead[1][cap])
                    else:
                        curr[buy][cap] = max(prices[i] + ahead[1][cap-1], 0+ ahead[0][cap])
                ahead = curr
        return ahead[1][2]
# Using Four Variable Solution
# Time Complexity is O(n)
# Sapce Complexity is O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy1, buy2 = float('inf'), float('inf')
        sell1 , sell2 = 0,0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        return sell2
