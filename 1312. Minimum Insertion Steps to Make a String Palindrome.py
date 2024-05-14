# Using Tabulation Method
# Time Complexity is O(n*n)
# Space Complexity is O(n*n)
class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1] )
        return dp[n][n]
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        lps = self.lcs(s, s1)
        return len(s) - lps
# Space Optimization Solution 
# Time Complexity is O(n*n)
# Space Complexity is O(n)
class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        prev, curr = [0]*(n+1), [0]*(n+1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1] )
            prev = curr[:]
        return prev[n]
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        lps = self.lcs(s, s1)
        return len(s) - lps