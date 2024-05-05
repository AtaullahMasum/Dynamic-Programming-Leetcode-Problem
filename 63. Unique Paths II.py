# using recursion 
# Time Compelxity is O(2^(m+n))
# Space Complexity is O((m-1)+(n-1))
class Solution:
    def helper(self, row, col, obstacleGrid):
        if row >= 0 and col >= 0 and obstacleGrid[row][col] == 1:
            return 0
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0:
            return 0
        up = self.helper(row-1, col, obstacleGrid)
        left = self.helper(row, col-1, obstacleGrid)
        return up + left
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        return self.helper(row-1, col-1, obstacleGrid)
# Using Memoization 
# Time Complexity is O(m*n)
# Space Complexity is O((m-1)+(n-1))+O(n*m)
class Solution:
    def helper(self, row, col, obstacleGrid, dp):   
        if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
            return 0
        if row == 0 and col == 0:
            return 1
        if dp[row][col] != -1:
            return dp[row][col]
        up = self.helper(row-1, col, obstacleGrid, dp)
        left = self.helper(row, col-1, obstacleGrid, dp)
        dp[row][col] = up + left
        return dp[row][col]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*col for _ in range(row)]
        return self.helper(row-1, col-1, obstacleGrid, dp)
# Using Tabulation Method
# Time Complexity is O(m*n)
# Space Complexity is O(m*n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up , left = 0, 0
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                    dp[i][j] = up+left
        return dp[row-1][col-1]
# Space Optimization 
# Time Complexity is(m*n)
# Space complexity is O(n)+O(n)
class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0]*col 
        for i in range(row):
            curr = [0]*col
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up , left = 0, 0
                    if i>0:
                        up = prev[j]
                    if j>0:
                        left = curr[j-1]
                    curr[j] = up+left
            prev = curr
        return prev[col-1]
