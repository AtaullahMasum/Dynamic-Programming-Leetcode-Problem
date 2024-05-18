# Using Recursion Method
# Time Complexity is O(2^n)
# Space Complexity is O(n)
class Solution:
    def helper(self,ind, buy, prices):
        if ind == len(prices):
            return 0
        profit = 0
        if buy:
            profit = max( -prices[ind] + self.helper(ind+1, 0, prices), 0 + self.helper(ind+1, 1, prices))
        else:
            profit = max(prices[ind] + self.helper(ind+1, 1, prices), 0 + self.helper(ind+1, 0, prices))
        return profit


    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, 1, prices)
# Using Memoization 
# Time Complexity is O(n*2)
# Space Complexity is O(n*2) + O(n)
class Solution:
    def helper(self,ind, buy, prices, dp):
        if ind == len(prices):
            return 0
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        profit = 0
        if buy:
            profit = max( -prices[ind] + self.helper(ind+1, 0, prices, dp), 0 + self.helper(ind+1, 1, prices, dp))
        else:
            profit = max(prices[ind] + self.helper(ind+1, 1, prices, dp), 0 + self.helper(ind+1, 0, prices, dp))
        dp[ind][buy] = profit
        return dp[ind][buy]


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        return self.helper(0, 1, prices,dp)
# Using Tabulation Method 
# Time Complexity is O(n*2)
# Space Complexity is O(n*2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n-1, -1, -1):
            profit = 0
            for buy in (0, 1):
                if buy:
                    profit = max(-prices[i] + dp[i+1][0],0+ dp[i+1][1])
                else:
                    profit = max(prices[i] + dp[i+1][1], 0+dp[i+1][0])
                dp[i][buy] = profit
        return dp[0][1]
# Sapce Optimization Method
# Time Complexity is O(n*2)
# Space Complexity is O(2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead, curr = [0]*2, [0]*2
        ahead[0] = ahead[1] = 0
        for i in range(n-1, -1, -1):
            profit = 0
            for buy in (0, 1):
                if buy:
                    profit = max(-prices[i] + ahead[0],0+ ahead[1])
                else:
                    profit = max(prices[i] + ahead[1], 0+ ahead[0])
                curr[buy] = profit
            ahead = curr[:]
        return ahead[1]
        