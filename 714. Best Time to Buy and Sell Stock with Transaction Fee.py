# Using Recursion Method
# Time Complexity is O(2^n) = exponentail
# Space Complexity is O(n)
class Solution:
    def helper(self, ind, buy, prices, fee):
        if ind == len(prices):
            return 0
        if buy :
            return max( -prices[ind] + self.helper(ind+1, 0, prices, fee), 0 + self.helper(ind+1, 1, prices, fee))
        else:
            return max(prices[ind] - fee + self.helper(ind+1, 1, prices, fee), 0 + self.helper(ind+1, 0, prices,fee))

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.helper(0, 1, prices, fee)
# Using Memoization Method
# Time Complexity is O(n*2)
# Space Complexity is (n*2) + O(n)
class Solution:
    def helper(self, ind, buy, prices, fee, dp):
        if ind == len(prices):
            return 0
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        if buy :
            dp[ind][buy] = max( -prices[ind] + self.helper(ind+1, 0, prices, fee, dp), 0 + self.helper(ind+1, 1, prices, fee, dp))
            return dp[ind][buy]
        else:
            dp[ind][buy] = max(prices[ind] - fee + self.helper(ind+1, 1, prices, fee, dp), 0 + self.helper(ind+1, 0, prices,fee, dp))
            return dp[ind][buy]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]
        return self.helper(0, 1, prices, fee, dp)
# Using Tabulation Method
# Time Complexity is O(n)
# Space Complexity is O(n*2)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*(2) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            # Buy
            dp[i][1] = max(-prices[i] + dp[i+1][0], 0+dp[i+1][1])
            # Sell
            dp[i][0] = max(prices[i]-fee + dp[i+1][1], 0+dp[i+1][0])
        return dp[0][1]
# Space Optimization
# Time Complexity is O(n)
# Space Complexity is O(2)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        front, curr = [0]*(2), [0]*(2) 
        for i in range(n-1, -1, -1):
            # Buy
            curr[1] = max(-prices[i] + front[0], 0+front[1])
            # Sell
            curr[0] = max(prices[i]-fee + front[1], 0+front[0])
            front = curr[:]
        return front[1]
# Using Four Varaible 
# Time Complexity is O(n)
# Sapce Compolexity is O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        frontNotBuy, frontBuy, currNotBuy, currBuy = 0,0,0,0
        for i in range(n-1, -1, -1):
            currNotBuy = max(prices[i]-fee + frontBuy, 0+frontNotBuy)
            currBuy = max(-prices[i] + frontNotBuy, 0+frontBuy)
            frontNotBuy = currNotBuy
            frontBuy = currBuy
        return frontBuy
        
        