# Using Recursion
# Time Complexity is O(2^(sumofallrows))
# Space Complexity is O(numofrows)
class Solution:
    def helper(self, i, j, triangle, n):
        if i == n-1:
            return triangle[n-1][j]
        d = triangle[i][j] + self.helper(i+1, j, triangle, n)
        dg = triangle[i][j] + self.helper(i+1, j+1, triangle, n)
        return min(d, dg)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        return self.helper(0,0, triangle, n)
# Using Memoization 
# Time Complexity is O(n*n)
# Space Complexity is O(sum of all rows) + O(n*n)
class Solution:
    def helper(self, i, j, triangle, n, dp):
        if i == n-1:
            return triangle[n-1][j]
        if dp[i][j] != -1:
            return dp[i][j]
        d = triangle[i][j] + self.helper(i+1, j, triangle, n, dp)
        dg = triangle[i][j] + self.helper(i+1, j+1, triangle, n, dp)
        dp[i][j] = min(d, dg)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp =[[-1 for _ in range(i+1)] for i in range(n)]
        return self.helper(0,0, triangle, n, dp)
# Tabulation Mehtod
# Time Complexity  O(n*n)
# Space Complexity is O(n*n)
class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        #dp =[[0 for _ in range(i+1)] for i in range(n)]
        dp = [[0] * len(row) for row in triangle]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                d = dp[i+1][j] + triangle[i][j]
                dg = dp[i+1][j+1] + triangle[i][j]
                dp[i][j] = min(d, dg)
        return dp[0][0]
# Space Optimization Method
# Time Complexity is O(n*n)
# Space Complexity is O(2*n)
class Solution: 
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        #dp =[[0 for _ in range(i+1)] for i in range(n)]
        front = [0]*n
        for j in range(n):
           front[j] = triangle[n-1][j]
        for i in range(n-2, -1, -1):
            curr = [0]*len(triangle[i])
            for j in range(i, -1, -1):
                d = front[j] + triangle[i][j]
                dg = front[j+1] + triangle[i][j]
                curr[j] = min(d, dg)
            front = curr
        return front[0]
