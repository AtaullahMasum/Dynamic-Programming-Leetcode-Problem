# Using Tabulation Method All Three Solution 
# Time Complexity is O(n*n)
# Space Complexity is O(n*n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]
        #Better Approch
        n = len(s)
        dp =[[0] *n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for gap in range(2, n+1):
            for i in range(n - gap+1):
                j = gap + i - 1
                if gap == 2 and s[i]== s[j]:
                    dp[i][j] = 2
           
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
        #Using LCS
        string = s[::-1]
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[j-1] == string[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][n]
        
