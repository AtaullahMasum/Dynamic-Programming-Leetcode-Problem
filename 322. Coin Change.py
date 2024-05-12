# Using Recursion 
# Time Complexity is >>O(2^n)
# Space Complexity is O(amount)
class Solution:
    def helper(self, ind, amount, coins):
        if ind == 0:
            if amount% coins[0]== 0:
                return amount//coins[0]
            else:
                return float('inf')
        not_take = 0 + self.helper(ind-1, amount, coins)
        take = float('inf')
        if coins[ind] <= amount:
            take  = 1 + self.helper(ind, amount- coins[ind], coins)
        return min(not_take, take)
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if not amount:
            return 0
        if self.helper(n-1, amount, coins) == float('inf'):
            return -1
        else:
            return self.helper(n-1, amount, coins)
# Using Memoization 
# Time Complexity is O(n*amount)
# Space Complexity is O(amount)+ O(n*amount)
class Solution:
    def helper(self, ind, amount, coins, dp):
        if ind == 0:
            if amount% coins[0]== 0:
                return amount//coins[0]
            else:
                return float('inf')
        if dp[ind][amount] != -1:
            return dp[ind][amount]
        not_take = 0 + self.helper(ind-1, amount, coins, dp)
        take = float('inf')
        if coins[ind] <= amount:
            take  = 1 + self.helper(ind, amount- coins[ind], coins, dp)
        dp[ind][amount] = min(not_take, take)
        return dp[ind][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if not amount:
            return 0
        dp = [[-1]*(amount+1) for _ in range(n)]
        if self.helper(n-1, amount, coins, dp) == float('inf'):
            return -1
        else:
            return self.helper(n-1, amount, coins, dp)
# Using Tabulation Method
# Time Complexity is O(n*amount)
# Space Complexity is O(n*amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if not amount:
            return 0
        dp = [[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i% coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float('inf')
        for i in range(1, n):
            for tar in range(amount+1):
                not_take = dp[i-1][tar]
                take = float('inf')
                if coins[i] <= tar:
                    take = 1 + dp[i][tar- coins[i]]
                dp[i][tar] = min(not_take, take)
        if dp[n-1][amount] == float('inf'):
            return -1
        else:
            return dp[n-1][amount]