# Time Complexity is O(m*n)
# Space Complexity is O(m*n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    maxArea = max(maxArea, dp[i][j])
        return maxArea*maxArea