# Using Recursion Method
# Time Complexity is >>O(2^n) = Exponential
# Space Complexity is O(W)
 
class Solution:
    def helper(self, ind, W, val, wt):
        if ind == 0:
            return (W//wt[0])*val[0]
        not_take = self.helper(ind-1, W, val, wt)
        take = float("-inf")
        if wt[ind] <= W:
            take = val[ind] + self.helper(ind, W- wt[ind], val, wt)
        return max(not_take, take)
    def knapSack(self, N, W, val, wt):
        # code here
        return self.helper(N-1, W, val, wt)
# Using Memoization Method
# Time Complexity is O(N*W)
# Space Complexity is O(N*W) + O(N)
 
class Solution:
    def helper(self, ind, W, val, wt, dp):
        if ind == 0:
            return (W//wt[0])*val[0]
        if dp[ind][W] != -1:
            return dp[ind][W]
        not_take = self.helper(ind-1, W, val, wt, dp)
        take = float("-inf")
        if wt[ind] <= W:
            take = val[ind] + self.helper(ind, W- wt[ind], val, wt, dp)
        dp[ind][W] = max(not_take, take)
        return dp[ind][W]
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[-1]*(W+1) for _ in range(N)]
        return self.helper(N-1, W, val, wt, dp)
# Using Tabulation Method
# Time Complexity is O(N*W)
# Space Complexity is O(N*W)
 
class Solution:
 
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[0]*(W+1) for _ in range(N)]
        for w in range(W+1):
            dp[0][w] = (w//wt[0])*val[0]
        for i in range(1, N):
            for w in range(W+1):
                not_take = dp[i-1][w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + dp[i][w - wt[i]]
                dp[i][w] = max(not_take, take)
        return dp[N-1][W]
# Using Space Optimization Method
# Time Complexity is O(N*W)
# Space Complexity is O(W)
class Solution:
 
    def knapSack(self, N, W, val, wt):
        # code here
        prev = [0]*(W+1) 
        curr = [0]*(W+1) 
        for w in range(W+1):
            prev[w] = (w//wt[0])*val[0]
        for i in range(1, N):
            for w in range(W+1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + curr[w - wt[i]]
                curr[w] = max(not_take, take)
            prev = curr
        return prev[W]
# Using Single 1D array Space 
# Time Complexity is O(N*W)
# Space Complexity is O(W)
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        prev = [0]*(W+1)   
        for w in range(W+1):
            prev[w] = (w//wt[0])*val[0]
        for i in range(1, N):
            for w in range(W+1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + prev[w - wt[i]]
                prev[w] = max(not_take, take)
        return prev[W]