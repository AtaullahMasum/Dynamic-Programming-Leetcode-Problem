# Using Recursion Method
# Time Complexity is O(2^m+2^n)
# Space Complexity is O(m+n)
class Solution:
    def helper(self, ind1, ind2, text1, text2):
        if ind1 == 0 or ind2 == 0:
            return 0
        if text1[ind1-1] == text2[ind2-1]:
            return 1 + self.helper(ind1-1, ind2-1, text1, text2)
        return 0 + max(self.helper(ind1-1, ind2, text1, text2), self.helper(ind1, ind2-1, text1, text2))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        return self.helper(m, n, text1, text2)
# Using Memoization Method
# Time Complexity is O(m*n)
# Space Complexity is O(m*n) + O(m+n)
class Solution:
    def helper(self, ind1, ind2, text1, text2, dp):
        if ind1 == 0 or ind2 == 0:
            return 0
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        if text1[ind1-1] == text2[ind2-1]:
            dp[ind1][ind2] = 1 + self.helper(ind1-1, ind2-1, text1, text2, dp)
            return dp[ind1][ind2]
        dp[ind1][ind2] = 0 + max(self.helper(ind1-1, ind2, text1, text2, dp), self.helper(ind1, ind2-1, text1, text2, dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return self.helper(m, n, text1, text2, dp)
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

        return dp[m][n]
# Using Space Optimization Method
# Time Complexity is O(m*n)
# Space Complexity is O(n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev , curr = [0]*(n+1), [0]*(n+1) 
        for i in range(n+1):
            prev[i] = 0
       
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = 0 + max(prev[j], curr[j-1])
            prev = curr[:]

        return prev[n]
