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