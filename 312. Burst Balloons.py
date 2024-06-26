# Using Recursion Method 
# Time Complexity is O(n*2^n) = exponential
# Space Complexity is O(n)
class Solution:
    def helper(self, i, j, nums):
        if i > j:
            return 0
        maxi = float('-inf')
        for ind in range(i, j+1):
            cost = nums[i-1]*nums[ind]*nums[j+1] + self.helper(i, ind-1, nums) + self.helper(ind+1, j, nums)
            maxi = max(maxi, cost)
        return maxi

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        return self.helper(1, n, nums)
# Using Memoization Method
# Time Complexity is O(n*n*n)
# Space Complexity is O(n*n)
class Solution:
    def helper(self, i, j, nums, dp):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi = float('-inf')
        for ind in range(i, j+1):
            cost = nums[i-1]*nums[ind]*nums[j+1] + self.helper(i, ind-1, nums, dp) + self.helper(ind+1, j, nums, dp)
            maxi = max(maxi, cost)
        dp[i][j] = maxi
        return dp[i][j]

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp = [[-1]*(n+2) for _ in range(n+2)]
        return self.helper(1, n, nums, dp)
# Using Tabulation Method
# Time Complexity is O(n*n*n)
# Space Complexity is O(n*n)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, 0, -1):
            for j in range(1, n+1):
                if i > j:
                    continue
                maxi = float('-inf')
                for ind in range(i, j+1):
                    cost = nums[i-1]*nums[ind]*nums[j+1] +dp[i][ind-1] + dp[ind+1][j]
                    maxi = max(maxi, cost)
                dp[i][j] = maxi          
        return dp[1][n]
