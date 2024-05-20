# Using Tabulation Method
# Time Complexity is O(n*n)
# Space Complexity is O(n*n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]* (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for prev_ind in range(i-1, -2, -1):
                lis = dp[i+1][prev_ind + 1]
                if prev_ind == -1 or nums[i] > nums[prev_ind]:
                    lis = max(lis, 1 + dp[i+1][i+1])
                dp[i][prev_ind +1] = lis
        return dp[0][0]
# Sapce Optimization
# Time Complexity is O(n*n)
# Space Complexity is O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        front, curr = [0]* (n+1), [0]* (n+1) 
        for i in range(n-1, -1, -1):
            for prev_ind in range(i-1, -2, -1):
                lis = front[prev_ind + 1]
                if prev_ind == -1 or nums[i] > nums[prev_ind]:
                    lis = max(lis, 1 + front[i+1])
                curr[prev_ind +1] = lis
            front = curr[:]
        
        return front[0]
# Using 1D dp 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        maxi = 0
        for i in range(n):
            for prev_ind in range(i):
                if nums[i] > nums[prev_ind]:
                    dp[i] = max(dp[i], 1 + dp[prev_ind])
            maxi = max(maxi, dp[i])
        return maxi
# Printing LIS 
class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        # Code here
        hashMap = [0]*N
        dp = [1]*N
        lastIndex = 0
        maxi = 1
        for i in range(N):
            hashMap[i] = i
            for prev_ind in range(i):
                if arr[i] > arr[prev_ind] and 1 + dp[prev_ind] > dp[i]:
                    dp[i] = 1 + dp[prev_ind]
                    hashMap[i] = prev_ind
            
            if maxi < dp[i]:
                maxi = dp[i]
                lastIndex = i
        lis = []
        lis.append(arr[lastIndex])
        while hashMap[lastIndex] != lastIndex:
            lastIndex = hashMap[lastIndex]
            lis.append(arr[lastIndex])
        return lis[::-1]