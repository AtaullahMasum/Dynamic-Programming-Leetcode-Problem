# Using Recursion Method
# Time Complexity is O(2^n)
# Space Complexity is O(n)
class Solution:
    def helper(self, ind, prev_ind, nums):
        if ind == len(nums):
            return 0
        lis = 0 + self.helper(ind+1, prev_ind, nums) # not take
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            lis = max(lis, 1 + self.helper(ind+1, ind, nums)) # take
        return lis
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(0, -1, nums)
# Using Memoization  Method
# Time Complexity is O(n*n)
# Space Complexity is O(n*n) + O(n)
class Solution:
    def helper(self, ind, prev_ind, nums, dp):
        if ind == len(nums):
            return 0
        if dp[ind][prev_ind + 1] != -1:
            return dp[ind][prev_ind+1]
        lis = 0 + self.helper(ind+1, prev_ind, nums, dp) # not take
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            lis = max(lis, 1 + self.helper(ind+1, ind, nums, dp)) # take
        dp[ind][prev_ind + 1] = lis
        return dp[ind][prev_ind + 1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]* n for _ in range(n+1)]
        return self.helper(0, -1, nums, dp)
# Using Tabulation Method
# Time Complexity is O(n*n)
# Sapce Complexity is O(n*n)
