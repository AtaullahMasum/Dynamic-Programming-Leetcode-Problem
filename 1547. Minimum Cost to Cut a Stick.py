# Using Recursion Method
# Time Complexity is O(2^n) = exponential 
# Sapce Complexity is O(n)
class Solution:
    def helper(self, i, j , cuts):
        if i > j:
            return 0
        mini = float('inf')
        for ind in range(i, j+1):
            cost = cuts[j+1] - cuts[i-1] + self.helper(i, ind-1, cuts) + self.helper(ind+1, j, cuts)
            mini = min(mini, cost)
        return mini
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        return self.helper(1, c, cuts)
# Using Memoization Method
# Time Complexity is O(n*n*n)
# Space Complexity is O(n*n) + O(n)

class Solution:
    def helper(self, i, j , cuts, dp):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for ind in range(i, j+1):
            cost = cuts[j+1] - cuts[i-1] + self.helper(i, ind-1, cuts, dp) + self.helper(ind+1, j, cuts, dp)
            mini = min(mini, cost)
        dp[i][j] = mini
        return dp[i][j]
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        dp = [[-1]*(c+1) for _ in range(c+1)]
        return self.helper(1, c, cuts, dp)
# Using Tabulation Method 
# Time Complexity is O(n*n*n)
# Space Complexity is O(n*n)
class Solution:
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        dp = [[0]*(c+2) for _ in range(c+2)]
        for i in range(c , 0, -1):
            for j in range(1 , c+1):
                if i > j:
                    continue
                mini = float('inf')
                for ind in range(i, j+1):
                    cost = cuts[j+1] - cuts[i-1] + dp[i][ind-1] + dp[ind+1][j]
                    mini = min(mini, cost)
                dp[i][j] = mini
        return dp[1][c] 
    