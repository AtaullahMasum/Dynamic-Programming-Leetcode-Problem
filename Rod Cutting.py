# Recursion Method
# Time Complexity is exponential >> O(2^n)
# Space Complexity is O(N)

class Solution:
    def helper(self, ind, n, price):
        if ind == 0:
            return n*price[0]
        not_take = 0+ self.helper(ind-1, n, price)
        take = float('-inf')
        rod_length = ind + 1
        if rod_length <= n:
            take = price[ind] + self.helper(ind, n-rod_length, price)
        return max(not_take, take)
    def cutRod(self, price, n):
        #code here
        N = len(price)
        return self.helper(N-1, n, price)
# Using Memoization Method
# Time Complexity is O(n*N)
# Space Complexity is O(n*N)
class Solution:
    def helper(self, ind, n, price, dp):
        if ind == 0:
            return n*price[0]
        if dp[ind][n] != -1:
            return dp[ind][n]
        not_take = 0+ self.helper(ind-1, n, price, dp)
        take = float('-inf')
        rod_length = ind + 1
        if rod_length <= n:
            take = price[ind] + self.helper(ind, n-rod_length, price, dp)
        dp[ind][n] =  max(not_take, take)
        return dp[ind][n]
    def cutRod(self, price, n):
        #code here
        N = len(price)
        dp = [[-1]*(n+1) for _ in range(N)]
        return self.helper(N-1, n, price, dp)
# Using Tabulation Method 
# Time Complexity is O(n*N)
# Space Complexity is (n*N)
class Solution:
    def cutRod(self, price, n):
        #code here
        N = len(price)
        dp = [[0]*(n+1) for _ in range(N)]
        for i in range(n+1):
            dp[0][i] = i*price[0]
        for i in range(1, N):
            for rod in range(n+1):
                not_take = dp[i-1][rod]
                take = float('-inf')
                rod_length = i+1
                if rod_length <= rod:
                    take = price[i] + dp[i][rod - rod_length]
                dp[i][rod] = max(not_take, take)
        return dp[N-1][n]
# Using 1D array 
# Time Complexity is O(n*N)
# Space Complexity is O(n)
class Solution:
    def cutRod(self, price, n):
        #code here
        N = len(price)
        prev = [0]*(n+1) 
        for i in range(n+1):
            prev[i] = i*price[0]
        for i in range(1, N):
            for rod in range(n+1):
                not_take = prev[rod]
                take = float('-inf')
                rod_length = i+1
                if rod_length <= rod:
                    take = price[i] + prev[rod - rod_length]
                prev[rod] = max(not_take, take)
        return prev[n]
#  Space and time  Optimization code
class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(i):
                max_val = max(max_val, price[j] + dp[i - j - 1])
            dp[i] = max_val
        return dp[n]

