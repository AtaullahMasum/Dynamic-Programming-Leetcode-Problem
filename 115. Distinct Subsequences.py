# Using Recursion Method
# Time Complexity is >>(2^n.2^m) = exponential 
# Space Complexity is O(n+m)
class Solution:
    def helper(self, i, j, s, t):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if s[i] == t[j]:
            return self.helper(i-1,j-1, s, t) + self.helper(i-1, j, s, t)
        else:
            return self.helper(i-1, j, s, t)
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        return self.helper(n-1, m-1, s, t)
# Using Memoization Method
# Time Complexity is O(n*m)
# Space Complexity is O(n*m) + O(n+m)
class Solution:
    def helper(self, i, j, s, t, dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.helper(i-1,j-1, s, t, dp) + self.helper(i-1, j, s, t, dp)
            return dp[i][j]
        else:
            dp[i][j] =  self.helper(i-1, j, s, t, dp)
            return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1]*(m) for _ in range(n)]
        return self.helper(n-1, m-1, s, t, dp)
# Using tabulation Method
# Time Complexity is O(n*m)
# Space Complexity is O(n*m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for j in range(1, m+1):
            dp[0][j] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]
# Using Space Optimization 
# Time Complexity is O(n*m)
# Space Complexity is O(m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        prev, curr = [0]*(m+1), [0]*(m+1)
        prev[0] = curr[0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr[:]
        return prev[m]
        