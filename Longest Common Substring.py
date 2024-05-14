# Using Tabulation Method 
# Time Complexity is O(n*m)
# Sapce Complexity is O(n*m)
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 0
        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans
# Space Optimization Method
# Time Complexity is O(n*m)
# Sapce Complexity is O(m)
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        prev, curr = [0]*(m+1) , [0]*(m+1)    
        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0
            prev = curr[:]
        return ans
            