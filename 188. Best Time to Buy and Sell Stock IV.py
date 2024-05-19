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
# Another Approch Using Recursion
# Time Complexity is O(2^n)
# Space Complexity is O(n)
class Solution:
    def helper(self,ind, trans, prices, k):
        if ind == len(prices) or trans == 2*k:
            return 0
        if trans%2==0:
            return max(-prices[ind] + self.helper(ind+1, trans+1, prices, k) , 0+ self.helper(ind+1, trans, prices, k))
        else:
            return max (prices[ind] + self.helper(ind+1, trans+1, prices, k), 0+self.helper(ind+1, trans, prices, k))
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.helper(0, 0, prices, k)
# Using Memoization Method
# Time Complexity is O(n*(2*k))
# Sapce Complexity is O(n*(2*k))+O(n)
class Solution:
    def helper(self,ind, trans, prices, k, dp):
        if ind == len(prices) or trans == 2*k:
            return 0
        if dp[ind][trans] != -1:
            return dp[ind][trans]
        if trans%2==0:
            dp[ind][trans] = max(-prices[ind] + self.helper(ind+1, trans+1, prices, k, dp) , 0+ self.helper(ind+1, trans, prices, k, dp))
            return dp[ind][trans]
        else:
            dp[ind][trans]= max (prices[ind] + self.helper(ind+1, trans+1, prices, k, dp), 0+self.helper(ind+1, trans, prices, k, dp))
            return dp[ind][trans]
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*(2*k) for _ in range(n)]
        return self.helper(0, 0, prices, k, dp)
# Using tabulation Method
# Time Complexity is O(n*(2*k))
# Space Complexity is O(n*(2*k))
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for trans in range(2*k-1, -1, -1):
                if trans%2==0:
                    dp[i][trans] = max(-prices[i] +dp[i+1][trans+1], 0+dp[i+1][trans])
                else:
                    dp[i][trans] = max(prices[i] + dp[i+1][trans+1], 0 + dp[i+1][trans])
        return dp[0][0]
# Using Space Optimization Method
# Time Complexity is O(n*(2*n))
# Space Complexity is O(2*k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead, curr = [0]*(2*k+1), [0]*(2*k+1)
        for i in range(n-1, -1, -1):
            for trans in range(2*k-1, -1, -1):
                if trans%2==0:
                    curr[trans] = max(-prices[i] +ahead[trans+1], 0+ahead[trans])
                else:
                    curr[trans] = max(prices[i] + ahead[trans+1], 0 + ahead[trans])
            ahead = curr[:]
        return ahead[0]
