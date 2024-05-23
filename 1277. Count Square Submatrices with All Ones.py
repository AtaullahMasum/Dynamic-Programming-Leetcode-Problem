# Time Complexity is O(m*n)
# Space Complexity is O(m*n)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += dp[i][j]
        return cnt
        