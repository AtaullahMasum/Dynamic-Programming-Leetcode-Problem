# Using Recursion Method
# Time Complexity is O(2^n) = exponential 
# Space Complexity is O(n)
class Solution:
    def helper(self, ind, buy, prices):
        if ind >= len(prices):
            return 0
        if buy:
            return max( -prices[ind]+ self.helper(ind+1, 0, prices), 0+self.helper(ind+1, 1, prices))
        else:
            return max(prices[ind] + self.helper(ind+2, 1, prices), 0+self.helper(ind+1, 0, prices))

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return self.helper(0, 1, prices)
# Using Memoization Method
# Time Complexity is O(n*2) 
# Space Complexity is O(n*2) + O(n)
class Solution:
    def helper(self, ind, buy, prices, dp):
        if ind >= len(prices):
            return 0
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        if buy:
            dp[ind][buy] = max( -prices[ind]+ self.helper(ind+1, 0, prices, dp), 0+self.helper(ind+1, 1, prices, dp))
            return dp[ind][buy]
        else:
            dp[ind][buy] = max(prices[ind] + self.helper(ind+2, 1, prices, dp), 0+self.helper(ind+1, 0, prices, dp))
            return dp[ind][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]
        return self.helper(0, 1, prices, dp)
# Using Tabulation Method 
# Time Complexity is O(n*2)
# Space Complexity is O(n*2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(2) for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[i][buy]  = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])
                else:
                    dp[i][buy] = max(prices[i] + dp[i+2][1] , 0+dp[i+1][0])
        return dp[0][1]
# Using Tabulation Method 
# Time Complexity is O(n)
# Space Complexity is O(n*2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(2) for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            dp[i][1]  = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])
            dp[i][0] = max(prices[i] + dp[i+2][1] , 0+dp[i+1][0])
        return dp[0][1]
# Space Optimization 
# Time Complexity is O(n)
# Space Complexity is O(2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        front1, front2, curr = [0]*(2), [0]*(2) , [0]*(2) 
        for i in range(n-1, -1, -1):
            curr[1]  = max(-prices[i] + front1[0], 0 + front1[1])
            curr[0] = max(prices[i] + front2[1] , 0+front1[0])
            front2 = front1[:]
            front1 = curr[:]
        return front1[1]
