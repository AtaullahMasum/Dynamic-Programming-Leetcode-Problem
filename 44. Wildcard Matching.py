# Using Recursion Method
# Time Complexity is O(3^n.3^m) = exponential
# Sapce Complexity is O(n+m)
class Solution:
    def helper(self, i, j, p, s):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if j < 0 and i >= 0:
            for i1 in range(i+1):
                if p[i1] != "*":
                    return False
            return True
        if p[i] == s[j] or p[i] == "?":
            return self.helper(i-1,j-1, p,s)
        if p[i] == "*":
            return self.helper(i-1, j, p, s) or self.helper(i, j-1, p, s)
        return False
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)
        return self.helper(m-1, n-1, p, s)
# Using Memoization Method
# Time Complexity is O(n*m)
# Space Complexity is O(n*m) + O(n+m)
class Solution:
    def helper(self, i, j, p, s, dp):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if j < 0 and i >= 0:
            for i1 in range(i+1):
                if p[i1] != "*":
                    return False
            return True
        if dp[i][j] != -1:
            return dp[i][j]
        if p[i] == s[j] or p[i] == "?":
            dp[i][j] = self.helper(i-1,j-1, p,s, dp)
            return dp[i][j]
        if p[i] == "*":
            dp[i][j] = self.helper(i-1, j, p, s, dp) or self.helper(i, j-1, p, s, dp)
            return dp[i][j]
        return False
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)
        dp = [[-1]*(n) for _ in range(m)]
        return self.helper(m-1, n-1, p, s, dp)
# Using tabulation Method
# Time Complexity is O(n*m)
# Space Complexity is O(n*m)
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            dp[0][j] = False
        for i in range(1, m+1):
            flag = True
            for i1 in range(1, i+1):
                if p[i1-1] != "*":
                    flag = False
                    break
            dp[i][0] = flag 
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]
# Space Optimization 
# Time Complexity is O(n*m)
# Space Complexity is O(n)
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        prev, curr = [False]*(n+1) , [False]*(n+1) 
        prev[0] = True
        for j in range(1, n+1):
            prev[j] = False      
        for i in range(1, m+1):
            flag = True
            for i1 in range(1, i+1):
                if p[i1-1] != "*":
                    flag = False
                    break
            curr[0] = flag
            for j in range(1, n+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    curr[j] = prev[j-1]
                elif p[i-1] == "*":
                    curr[j] = prev[j] or curr[j-1]
                else:
                    curr[j] = False
            prev = curr[:]
        return prev[n]