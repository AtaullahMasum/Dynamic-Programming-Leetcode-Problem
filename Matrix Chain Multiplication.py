# Using Recursion Method
# Time Complexity is O(2^n) = exponential
# Space Complexity is O(n)

class Solution:
    def helper(self, i, j, arr):
        if i == j:
            return 0
        mini = float('inf')
        for k in range(i, j):
            steps = arr[i-1]*arr[k]*arr[j] + self.helper(i, k, arr) + self.helper(k+1, j, arr)
            mini = min(mini, steps)
        return mini
        
            
    def matrixMultiplication(self, N, arr):
        # code here
        return self.helper(1, N-1, arr)
# Using Memoization Method
# Time Complexity is O(n*n*n)
# Sapce Complexity is O(n*n)
class Solution:
    def helper(self, i, j, arr, dp):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for k in range(i, j):
            steps = arr[i-1]*arr[k]*arr[j] + self.helper(i, k, arr, dp) + self.helper(k+1, j, arr, dp)
            mini = min(mini, steps)
        dp[i][j] = mini
        return dp[i][j]
        
            
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*N for _ in range(N)]
        return self.helper(1, N-1, arr, dp)
# Using Tabulation Method
# Time Complexity is O(n*n*n)
# Sapce Complexity is O(n*n)
class Solution:
   
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[0]*N for _ in range(N)]   
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                mini = float('inf')
                for k in range(i, j):
                    steps = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                    mini = min(mini, steps)
                dp[i][j] = mini
        return dp[1][N-1]