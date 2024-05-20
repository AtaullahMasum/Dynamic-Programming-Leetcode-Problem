# These solution is not follow by strictly incresing order followed by strictly decreasing order
from typing import List


class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        dp1 = [1]*n
        dp2 = [1]*n
        for i in range(n):
            for prev in range(i):
                if nums[i] > nums[prev] :
                    dp1[i] = max(dp1[i], 1 + dp1[prev])
       
        for i in range(n-1, -1, -1):
            for prev in range(n-1, i, -1):
                if nums[i] > nums[prev] :
                    dp2[i] = max(dp2[i], 1 + dp2[prev])
        
        maxi = -1
        for i in range(n):
            maxi = max(maxi, dp1[i] + dp2[i] -1)
        return maxi
# Solution 2
class Solution:

    def LongestBitonicSequence(self, n, nums):
        lis = [1] * n
        # Compute LIS values from left to right
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1  # updating LIS value for current index

        lds = [1] * n
        # Compute LDS values from right to left
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j] and lds[i] < lds[j] + 1:
                    lds[i] = lds[j] + 1  # updating LDS value for current index

        # Return the maximum value of lis[i] + lds[i] - 1
        ans = 0  # initializing ans with length of longest bitonic sequence
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                ans = max(
                    ans, lis[i] + lds[i] - 1
                )  # updating ans if current index has non-zero values for both LIS and LDS
        return ans
    