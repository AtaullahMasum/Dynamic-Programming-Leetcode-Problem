# Using recursion solution
# Time Complexity is O(4*n*n)
# Space Complexity is O(n*n*n)
class Solution:
    # dfs 
    def helper(self, r1, c1, c2, grid, n, dp):
        r2 = r1 + c1 - c2
        if r1 >= n or r2 >= n or c1 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        if r1 == n-1 and c1 == n-1:
            return grid[r1][c1]
        if dp[r1][c1][c2] != -2:
            return dp[r1][c1][c2]
        cherries = grid[r1][c1]
        if r1 != r2:
            cherries += grid[r2][c2]
        right_right = self.helper(r1, c1+1, c2+1, grid, n, dp)
        right_down = self.helper(r1, c1+1, c2, grid, n, dp)
        down_right = self.helper(r1+1, c1, c2+1, grid, n, dp)
        down_down = self.helper(r1+1, c1, c2, grid, n, dp)
        dp[r1][c1][c2] = cherries + max(right_right, right_down, down_right, down_down)
        return dp[r1][c1][c2]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-2]*n for _ in range(n)] for _ in range(n)]
        return max(0,self.helper(0,0,0, grid, n, dp))
        