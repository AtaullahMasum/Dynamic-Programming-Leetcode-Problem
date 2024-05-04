# Tabulation method 
# Time complexity: O(n*m)
# Space complexity: O(n*m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)] #mxn
       
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up , left = 0,0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[-1][-1]
# Space Optimization
# Time Complexity is O(n*m)
# Space Complexity is O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*n
       
        for i in range(m):
            temp = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                else:
                    up , left = 0,0
                    if i > 0:
                        up = dp[j]
                    if j > 0:
                        left = temp[j - 1]
                    temp[j] = up + left
            dp = temp           
        return dp[-1]
        