# Using Recursion Method
# Time Complexity is O(n*2^n) = exponential
# Space Complexity is  O(n)
# https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1
class Solution:
    def helper(self, i, j, isTrue, s):
        if i > j:
            return 0
        if i == j:
            if isTrue:
                return 1 if s[i] == 'T' else 0
            else:
                return  1 if s[i] == 'F' else 0
        
        ways = 0
        for ind in range(i+1, j, 2):
            leftTrue = self.helper(i, ind-1, 1, s)%1003
            leftFalse = self.helper(i, ind-1, 0, s)%1003
            rightTrue = self.helper(ind+1, j, 1, s)%1003
            rightFalse = self.helper(ind+1, j, 0, s)%1003
            if s[ind] == '&':
                if isTrue:
                    ways += (leftTrue*rightTrue)%1003
                else:
                    ways += (((leftFalse*rightTrue)%1003)+((leftTrue*rightFalse)%1003)+((leftFalse*rightFalse)%1003)%1003)
            elif s[ind] == '|':
                if isTrue:
                    ways += ((leftTrue*rightFalse)%1003 + (leftTrue*rightTrue)%1003+(leftFalse*rightTrue)%1003)%1003
                else:
                    ways += (leftFalse*rightFalse)%1003
            else:
                if isTrue:
                    ways += ((leftFalse*rightTrue)%1003 + (leftTrue*rightFalse)%1003)%1003
                else:
                    ways += ((leftFalse*rightFalse)%1003 +(leftTrue*rightTrue)%1003)%1003
        return ways
                
    def countWays(self, n, s):
        # code here
        return self.helper(0, n-1, 1, s)
# Using Memoization Method
# Time Complexity is O(n*n*n*2) = O(n^3)
# Space Complexity is O(n*n*2) = O(n^2) + O(n)
class Solution:
    def helper(self, i, j, isTrue, s, dp):
        if i > j:
            return 0
        if i == j:
            if isTrue:
                return  int(s[i] == 'T')
            else:
                return  int (s[i] == 'F')
        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]
        ways = 0
        for ind in range(i+1, j, 2):
            lt = self.helper(i, ind-1, 1, s, dp)
            lf = self.helper(i, ind-1, 0, s, dp)
            rt= self.helper(ind+1, j, 1, s, dp)
            rf = self.helper(ind+1, j, 0, s, dp)
            if s[ind] == '&':
                if isTrue:
                    ways = (ways +(lt*rt)%1003)%1003
                else:
                    ways = (ways+ (lf*rt)%1003+(lt*rf)%1003+(lf*rf)%1003)%1003
            elif s[ind] == '|':
                if isTrue:
                    ways = (ways+ (lt * rt)%1003 + (lf*rt)%1003+(lt*rf)%1003)%1003
                else:
                    ways = (ways+ (lf*rf)%1003)%1003
            else:
                if isTrue:
                    ways = (ways+ (lf*rt)%1003 + (lt*rf)%1003)%1003
                else:
                    ways = (ways + (lf*rf)%1003 +(lt*rt)%1003)% 1003
        dp[i][j][isTrue] = ways
        return dp[i][j][isTrue]
                
    def countWays(self, n, s):
        dp = [[[-1]*2 for _ in range(n)] for _ in range(n)]
        return self.helper(0, n - 1, 1, s, dp)
# Simple Modified
class Solution:
    def helper(self, i, j, isTrue, s, dp):
        if i > j:
            return 0
        if i == j:
            if isTrue:
                return int(s[i] == 'T')
            else:
                return int(s[i] == 'F')
        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]

        ways = 0
        for ind in range(i+1, j, 2):
            lt = self.helper(i, ind-1, 1, s, dp)
            lf = self.helper(i, ind-1, 0, s, dp)
            rt = self.helper(ind+1, j, 1, s, dp)
            rf = self.helper(ind+1, j, 0, s, dp)

            if s[ind] == '&':
                if isTrue:
                    ways = (ways + lt * rt) % 1003
                else:
                    ways = (ways + lf * rt + lt * rf + lf * rf) % 1003
            elif s[ind] == '|':
                if isTrue:
                    ways = (ways + lt * rt + lf * rt + lt * rf) % 1003
                else:
                    ways = (ways + lf * rf) % 1003
            elif s[ind] == '^':
                if isTrue:
                    ways = (ways + lf * rt + lt * rf) % 1003
                else:
                    ways = (ways + lf * rf + lt * rt) % 1003

        dp[i][j][isTrue] = ways
        return dp[i][j][isTrue]
                
    def countWays(self, n, s):
        dp = [[[-1]*2 for _ in range(n)] for _ in range(n)]
        return self.helper(0, n - 1, 1, s, dp)
# Using Tabulation Method 
# Time Compelxity is O(n^3)
# Space Complexity is O(n^2)
class Solution:
    def countWays(self, n, exp):
        n = len(exp)
        mod = 1003
        
        # Create a 3D DP array to store the results of subproblems
        dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        
        # Iterate over the expression string
        for i in range(n - 1, -1, -1):
            for j in range(n):
                # Base case 1: Skip invalid ranges
                if i > j:
                    continue
                
                # Iterate over possible values of 'isTrue' (0 or 1)
                for isTrue in range(2):
                    # Base case 2: When i == j
                    if i == j:
                        if isTrue == 1:
                            dp[i][j][isTrue] = int(exp[i] == 'T')
                        else:
                            dp[i][j][isTrue] = int(exp[i] == 'F')
                        continue
                    
                    # Recurrence logic
                    ways = 0
                    for ind in range(i + 1, j, 2):
                        lT = dp[i][ind - 1][1]
                        lF = dp[i][ind - 1][0]
                        rT = dp[ind + 1][j][1]
                        rF = dp[ind + 1][j][0]
    
                        if exp[ind] == '&':
                            if isTrue:
                                ways = (ways + (lT * rT) % mod) % mod
                            else:
                                ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lF * rF) % mod) % mod
                        elif exp[ind] == '|':
                            if isTrue:
                                ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lT * rT) % mod) % mod
                            else:
                                ways = (ways + (lF * rF) % mod) % mod
                        else:
                            if isTrue:
                                ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod
                            else:
                                ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod
                    
                    dp[i][j][isTrue] = ways
        
        # The final result is stored in dp[0][n - 1][1] when the expression is considered true
        return dp[0][n - 1][1]
                


