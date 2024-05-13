# Using Recursion
# Time Complexity is >> O(2^n) = exponential
# Space Complexity is O(amount)
class Solution:
    # dfs 
    def helper(self, ind, amount, coins):
        if ind == 0:
            if amount%coins[0] == 0:
                return 1
            else:
                return 0
        not_take = self.helper(ind-1, amount, coins)
        take = 0
        if coins[ind] <= amount:
            take = self.helper(ind, amount - coins[ind], coins)
        return not_take + take
        
    def change(self, amount: int, coins: List[int]) -> int:
        return self.helper(len(coins)-1, amount, coins)
# Using Memoization Method
# Time Complexity is O(n*amount)
# Space Complexity is (n*amount) + O(amount)
class Solution:
    # dfs 
    def helper(self, ind, amount, coins, dp):
        if ind == 0:
            if amount%coins[0] == 0:
                return 1
            else:
                return 0
        if dp[ind][amount] != -1:
            return dp[ind][amount]
        not_take = self.helper(ind-1, amount, coins, dp)
        take = 0
        if coins[ind] <= amount:
            take = self.helper(ind, amount - coins[ind], coins, dp)
        dp[ind][amount] = not_take + take
        return dp[ind][amount]
        
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        return self.helper(n-1, amount, coins, dp)
# Using Tabulation Method
# Time Complexity is O(n*amount)
# Space Complexity is (n*amount)
class Solution:        
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1
        for i in range(1, n):
            for tar in range(amount+1):
                not_take = dp[i-1][tar]
                take = 0
                if coins[i] <= tar:
                    take = dp[i][tar - coins[i]]
                dp[i][tar] = not_take + take
        return dp[n-1][amount]
# Space Optimization Solution
# Time Complexity is O(n*amount)
# Space Complexity is O(amount)
class Solution:        
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)
        for i in range(amount+1):
            if i % coins[0] == 0:
                prev[i] = 1
        for i in range(1, n):
            for tar in range(amount+1):
                not_take = prev[tar]
                take = 0
                if coins[i] <= tar:
                    take = curr[tar - coins[i]]
                curr[tar] = not_take + take
            prev = curr
        return prev[amount]
# Space Optimization Using Single Array
# Time Complexity is O(n*amount)
# Space Complexity is O(amount)
class Solution:        
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0]*(amount+1)
        for i in range(amount+1):
            if i % coins[0] == 0:
                prev[i] = 1
        for i in range(1, n):
            for tar in range(amount+1):
                not_take = prev[tar]
                take = 0
                if coins[i] <= tar:
                    take = prev[tar - coins[i]]
                prev[tar] = not_take + take
        return prev[amount]

        
