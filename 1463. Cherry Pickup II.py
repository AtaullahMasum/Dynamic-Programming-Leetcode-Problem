# Using Recursion
# Time Complexity is O(3^n x 3^n)
# Space Complexity is O(n)
class Solution:
    #dfs 
    def helper(self, r1, c1, c2, r, c, grid):
        if c1 < 0 or c1 >= c or c2 < 0 or c2 >= c:
            return float('-inf')
        if r1 == r-1:
            if c1 == c2 :
                return grid[r1][c1]
            else:
                return grid[r1][c1] + grid[r1][c2]
        maxi = float('-inf')
        for dc1 in (-1, 0, 1):
            for dc2 in (-1, 0, 1):
                value = 0
                if c1 == c2:
                    value = grid[r1][c1]
                else:
                    value = grid[r1][c1] + grid[r1][c2]
                value += self.helper(r1+1, c1+dc1, c2+dc2, r, c, grid)
                maxi = max(maxi, value)
        return maxi
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        return self.helper(0,0,c-1, r, c, grid)
        
# using Memoization 
# Time Complexity is O(n*m*3*3)
# Space Complexity is O(n^3) + O(n)
class Solution:
    #dfs 
    def helper(self, r1, c1, c2, r, c, grid, dp):
        if c1 < 0 or c1 >= c or c2 < 0 or c2 >= c:
            return float('-inf')
        if r1 == r-1:
            if c1 == c2 :
                return grid[r1][c1]
            else:
                return grid[r1][c1] + grid[r1][c2]
        if dp[r1][c1][c2] != -1:
            return dp[r1][c1][c2]
        maxi = float('-inf')
        for dc1 in (-1, 0, 1):
            for dc2 in (-1, 0, 1):
                value = 0
                if c1 == c2:
                    value = grid[r1][c1]
                else:
                    value = grid[r1][c1] + grid[r1][c2]
                value += self.helper(r1+1, c1+dc1, c2+dc2, r, c, grid, dp)
                maxi = max(maxi, value)
        dp[r1][c1][c2]= maxi
        return dp[r1][c1][c2]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[[-1]*c for _ in range(c)] for _ in range(r)]
        return self.helper(0,0,c-1, r, c, grid, dp)
        