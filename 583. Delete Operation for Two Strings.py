# Using Tabulation Method 
# Time Complexity is O(n*m)
# Sapce Complexity is O(n*m)
class Solution:
    def lcs (self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.lcs(word1, word2)
        deletions = len(word1) - lcs
        insertions = len(word2) - lcs
        return deletions + insertions
# Using Space Optimization
# Time Complexity is O(n*m)
# Space Complexity is O(n)
class Solution:
    def lcs (self, word1, word2):
        n, m = len(word1), len(word2)
        prev, curr = [0]*(m+1) , [0]*(m+1) 

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return prev[m]

    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.lcs(word1, word2)
        deletions = len(word1) - lcs
        insertions = len(word2) - lcs
        return deletions + insertions