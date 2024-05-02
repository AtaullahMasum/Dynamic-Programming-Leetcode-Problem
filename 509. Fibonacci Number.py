# Solution 1
# Time Complexity is O(n)
# Space Complexity is O(n) + O(n)
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
# Solution 2
# Time Complexity is O(n)
# Space Complexity is : O(n)
class Solution:   
    def fib(self, n: int) -> int:
        if n== 0:
            return 0
        if n == 1:
            return 1
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# Solution 3
# Time COmplexity is O(n)
# Space Complexity is O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        prev2 = 0
        prev1 = 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1
