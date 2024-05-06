# Using Recursion 
# Time Complexity is O(3^n)
# Space Complexity is O(n) 
class Solution:
    # DFS
    def helper(self, i, j, matrix):
        if j < 0 or j >= len(matrix[0]):
            return float('inf')
        if i == 0:
            return matrix[0][j]
        up = matrix[i][j] + self.helper(i-1, j, matrix)
        leftDiagonal = matrix[i][j] + self.helper(i-1, j-1, matrix)
        rightDiagonal = matrix[i][j] + self.helper(i-1, j+1, matrix)
        return min(up, leftDiagonal, rightDiagonal)
         
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        min_val = float('inf')
        for j in range(cols):
            min_val = min(min_val, self.helper(rows-1, j, matrix))
        return min_val
# Using Memoization 
# Time Complexity is O(n*m)
# Space Complexity is O(n) + O(n*m)
class Solution:
    # DFS
    def helper(self, i, j, matrix, dp):
        if j < 0 or j >= len(matrix[0]):
            return float('inf')
        if i == 0:
            return matrix[0][j]
        if dp[i][j] != -101:
            return dp[i][j]
        up = matrix[i][j] + self.helper(i-1, j, matrix, dp)
        leftDiagonal = matrix[i][j] + self.helper(i-1, j-1, matrix, dp)
        rightDiagonal = matrix[i][j] + self.helper(i-1, j+1, matrix, dp)
        dp[i][j] = min(up, leftDiagonal, rightDiagonal)
        return dp[i][j]
         
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-101]*cols for _ in range(rows)]
        min_val = float('inf')
        for j in range(cols):
            min_val = min(min_val, self.helper(rows-1, j, matrix, dp))
        return min_val
        
# Opitmal Solution using Dynamic Programming 
# Time Complexity is O(n*m)
# Space Complexity is O(n*m)
class Solution:
   
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for j in range(cols):
            dp[0][j] = matrix[0][j]
        for i in range(1,rows):
            for j in range(cols):
                leftDiagonal, rightDiagonal = float('inf'), float('inf')
                up = matrix[i][j] + dp[i-1][j]
                if j-1 >= 0:
                    leftDiagonal = matrix[i][j] + dp[i-1][j-1]
                if j+1 < cols:
                    rightDiagonal = matrix[i][j] + dp[i-1][j+1]
                dp[i][j] = min(up, leftDiagonal, rightDiagonal)
        return min(dp[-1])
    
# Space Optimization 
# Time Complexity is O(n*m)
# Space Complexity is O(2*m)
class Solution:
   
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev = [0]*cols 
        for j in range(cols):
            prev[j] = matrix[0][j]
        for i in range(1,rows):
            curr = [0]*cols
            for j in range(cols):
                leftDiagonal, rightDiagonal = float('inf'), float('inf')
                up = matrix[i][j] + prev[j]
                if j-1 >= 0:
                    leftDiagonal = matrix[i][j] + prev[j-1]
                if j+1 < cols:
                    rightDiagonal = matrix[i][j] + prev[j+1]
                curr[j] = min(up, leftDiagonal, rightDiagonal)
            prev = curr
        return min(prev)

        