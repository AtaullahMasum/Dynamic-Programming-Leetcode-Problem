# Opitmal Solution using Dynamic Programming 
# Time Complexity is O(nxnx3) = O(3n^2) = O(n^2)
# Space Complexity is O(n^2)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        direction = [(-1,0),(-1, -1), (-1, 1)]
        rows , cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for j in range(cols):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, rows):
           for j in range(cols):
              min_val = float('inf')
              for  r, c in direction:
                    prev_r = i + r
                    prev_c = j + c
                    if 0 <= prev_c < cols:
                        min_val = min(min_val, dp[prev_r][prev_c])
                    dp[i][j] = min_val + matrix[i][j]

                    
        return min(dp[-1])
        