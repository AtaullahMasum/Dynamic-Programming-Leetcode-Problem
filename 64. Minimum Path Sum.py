# Using Recursion
# Time Complexity is O(2^(m*n))
# Space Complexity is O(path sum) = O((m-1)+(n-1))
class Solution:
    def helper(self, i, j , grid):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        up = grid[i][j] + self.helper(i-1, j, grid)
        left = grid[i][j] + self.helper(i, j-1, grid)
        return min(up, left)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.helper(m-1, n-1, grid)
# Using Memoization 
# Time Complexity is O(m*n)
# Space Complexity is O((m*n))+ O(path Sum)
class Solution:
    def helper(self, i, j , grid, dp):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        up = grid[i][j] + self.helper(i-1, j, grid, dp)
        left = grid[i][j] + self.helper(i, j-1, grid, dp)
        dp[i][j] = min(up, left)
        return dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        return self.helper(m-1, n-1, grid, dp)
# Using Tabulation
# Time Complexity is O(m*n)
# Space Complexity is O(m*n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up , left = grid[i][j], grid[i][j]
                    if i > 0:
                        up += dp[i-1][j]
                    else:
                        up += float('inf')
                    if j > 0:
                        left += dp[i][j-1]
                    else:
                        left += float('inf')
                    dp[i][j] = min(up, left)
        return dp[m-1][n-1]
        