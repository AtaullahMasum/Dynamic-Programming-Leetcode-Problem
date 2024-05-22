# Using Recursion Method
# Time Complexity is O(2^n) = exponentail
# Space Complexity is O(n)
class Solution:
    def helper(self, ind, arr, n, k):
        if ind == n:
            return 0
        maxAns = float('-inf')
        maxi = float('-inf')
        Len = 0
        for j in range(ind, min(ind+k, n)):
            Len += 1
            maxi = max(maxi, arr[j])
            Sum = Len*maxi + self.helper(j+1, arr, n, k)
            maxAns = max(maxAns, Sum)
        return maxAns
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        return self.helper(0, arr, n, k)
# Using Memoization Method
# Time Complexity is O(n*n)
# Space Complexity is O(n)+O(n)
class Solution:
    def helper(self, ind, arr, n, k, dp):
        if ind == n:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        maxAns = float('-inf')
        maxi = float('-inf')
        Len = 0
        for j in range(ind, min(ind+k, n)):
            Len += 1
            maxi = max(maxi, arr[j])
            Sum = Len*maxi + self.helper(j+1, arr, n, k,dp)
            maxAns = max(maxAns, Sum)
        dp[ind] = maxAns
        return dp[ind]
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*(n)
        return self.helper(0, arr, n, k, dp)
# Using Tabulation Method
# Time Complexity is O(n*n)
# Space Complexity is O(n)
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for ind in range(n-1, -1, -1):
            maxAns = float('-inf')
            maxi = float('-inf')
            Len = 0
            for j in range(ind, min(ind+k, n)):
                Len += 1
                maxi = max(maxi, arr[j])
                Sum = Len*maxi + dp[j+1]
                maxAns = max(maxAns, Sum)
            dp[ind] = maxAns
        return dp[0]