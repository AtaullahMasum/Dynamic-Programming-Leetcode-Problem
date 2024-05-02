# Solution 1
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def fibonacci(self, n, dp):
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n] 
        dp[n] = self.fibonacci(n-1, dp) + self.fibonacci(n-2, dp)
        return dp[n]
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.fibonacci(n,dp)