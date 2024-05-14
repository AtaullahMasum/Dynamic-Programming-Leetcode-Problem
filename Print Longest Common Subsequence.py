# Using Tabulation Method
# Time Complexity is O(m*n)
# Space Complexity is O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 0
        for j in range(m+1):
            dp[j][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j], dp[i][j-1])
       # Backtracing step
        i, j = m, n
        string = ""
        
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                string += text1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else: # dp[i][j-1] > dp[i-1][j]
                j -= 1
        print(string[::-1])
# Print All LCS  