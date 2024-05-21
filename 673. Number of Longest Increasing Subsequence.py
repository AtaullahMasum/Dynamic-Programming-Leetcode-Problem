# Using Tabulation Method
# Time Complexity is O(n*n)
# Space Complexity is O(n) + O(n)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n
        maxi = 1
        for i in range(1, n):
            for prev in range(i):
                if nums[i] > nums[prev] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    cnt[i] = cnt[prev]
                elif nums[i] > nums[prev] and 1 + dp[prev] == dp[i]:
                    cnt[i] += cnt[prev]
            if maxi < dp[i]:
                maxi = dp[i]
        nolis = 0
        for i in range(n):
            if dp[i] == maxi:
                nolis += cnt[i]
        return nolis
        