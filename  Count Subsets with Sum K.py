# Using Recursion 
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from typing import List
def helper(ind, k, arr):
    if k == 0:
        return 1
    if ind == 0:
        if arr[0] == k:
            return 1
        else:
            return 0
    not_peak = helper(ind-1, k  , arr)
    peak = 0
    if arr[ind] <= k:
        peak = helper(ind - 1, k - arr[ind], arr)
    return not_peak + peak

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    return helper(n-1, k, arr)
# If array contain 0 then 
# Memoization 
from typing import List
def helper(ind, k, arr, dp):
    if ind == 0:
        if k == 0 and arr[0] == 0:
            return 2
        if k == arr[0] or k == 0:
            return 1
        return 0
    if dp[ind][k] != -1:
        return dp[ind][k]
    not_peak = helper(ind-1, k, arr, dp)
    peak = 0
    if arr[ind]<= k:
        peak = helper(ind-1, k - arr[ind], arr, dp)
    dp[ind][k] = (not_peak + peak)%(10**9 + 7)
    return dp[ind][k]

def findWays(arr: List[int], k: int) -> int:
    n  = len(arr)
    dp = [[-1]*(k+1) for _ in range(n)]

    return helper(n-1, k , arr, dp)
   
# Using Memoization
# Time Complexity is O(n*k)
# Space Complexity is O(n*k) + O(n)
from typing import List

def helper(ind, k, arr, dp):
    if k == 0:
        return 1
    if ind == 0:
        if arr[0] == k:
            return 1
        else:
            return 0
    if dp[ind][k] != -1:
        return dp[ind][k]
    not_peak = helper(ind - 1, k, arr, dp)
    peak = 0
    if arr[ind] <= k:
        peak = helper(ind - 1, k - arr[ind], arr, dp)
    dp[ind][k] =( not_peak + peak) %(10 **9 + 7)
    return dp[ind][k]

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1] * (k + 1) for _ in range(n)]
    return helper(n - 1, k, arr, dp)

    