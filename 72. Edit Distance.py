# Using Recursion Method
# Time Coomplexity is O(3^n.3^m) = exponentail
# Space Complexity is O(n+m)
class Solution:
    def helper(self, i, j, word1, word2):
        if i < 0:
            return j + 1
        if j < 0:
            return i +1
        if word1[i] == word2[j]:
            return 0 + self.helper(i-1, j-1, word1, word2)
        else:
            return 1 + min(self.helper(i-1,j, word1, word2), self.helper(i, j-1,word1, word2), self.helper(i-1, j-1, word1, word2))
        
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        return self.helper(n-1, m-1, word1, word2)
# Using Memoization Method
# Time Coomplexity is O(n*m) 
# Space Complexity is O(n*m) + O(n+m)
class Solution:
    def helper(self, i, j, word1, word2, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i +1
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            dp[i][j] = 0 + self.helper(i-1, j-1, word1, word2, dp)
            return dp[i][j]
        else:
            dp[i][j] = 1 + min(self.helper(i-1,j, word1, word2, dp), self.helper(i, j-1,word1, word2, dp), self.helper(i-1, j-1, word1, word2, dp))
            return dp[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp =[[-1]*m for _ in range(n)]
        return self.helper(n-1, m-1, word1, word2, dp)
# Using Memoization Method Using 1 Based Indexing
# Time Coomplexity is O(n*m) 
# Space Complexity is O(n*m) + O(n+m)
class Solution:
    def helper(self, i, j, word1, word2, dp):
        if i == 0:
            return j 
        if j == 0:
            return i 
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i-1] == word2[j-1]:
            dp[i][j] = 0 + self.helper(i-1, j-1, word1, word2, dp)
            return dp[i][j]
        else:
            dp[i][j] = 1 + min(self.helper(i-1,j, word1, word2, dp), self.helper(i, j-1,word1, word2, dp), self.helper(i-1, j-1, word1, word2, dp))
            return dp[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp =[[-1]*(m+1) for _ in range(n+1)]
        return self.helper(n, m, word1, word2, dp)
        
# Using Tabulation Method
# Time Coomplexity is O(n*m)
# Space Complexity is O(n*m)
class Solution: 
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp =[[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = j
        for i in range(n+1):
            dp[i][0] = i
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 0 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[n][m]

# Using Space Optimization 1D array
# Time Coomplexity is O(n*m)
# Space Complexity is O(m) + O(m)
class Solution: 
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev, curr =[0]*(m+1) , [0]*(m+1)
        for j in range(m+1):
            prev[j] = j
        
        for i in range(1, n+1):
            curr[0] = i
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = 0 + prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
            prev = curr[:]
        return prev[m]
