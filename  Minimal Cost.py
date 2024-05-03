# Using recursive solution
# Time Compelxity is O(n^k)
# Space Complexity is O(n)
from typing import List

def helper(index, k, heights):
    if index == 0:
        return 0
    minsteps = float('inf')
    for j in range(1, k+1):
        if index - j >= 0:
            jump = helper(index - j, k, heights) + abs(heights[index] - heights[index-j])
            minsteps = min(minsteps, jump)
    return minsteps

def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    return helper(n-1, k, heights)
# Using Recursion + Memoization 
# Time Compelxity is O(n*k)
# Space Compelxity is O(n)+O(n)
from typing import List

def helper(index, k, heights, dp):
    if index == 0:
        return 0
    if dp[index] != -1:
        return dp[index]

    minsteps = float('inf')
    for j in range(1, k+1):
        if index - j >= 0:
            jump = helper(index - j, k, heights, dp) + abs(heights[index] - heights[index-j])
            minsteps = min(minsteps, jump)
    dp[index] = minsteps
    return dp[index]

def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    dp = [-1]*n
    return helper(n-1, k, heights, dp)
# Using Tabulation Method
# Time Complexity is O(n*k)
# Space Compelxity is O(n)
from typing import List
def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    dp = [-1]*n
    dp[0] = 0
    for i in range(1, n):
        minsteps = float('inf')
        for j in range(1, k+1):
            if i - j >= 0:
                jump = dp[i-j] + abs(heights[i] - heights[i-j])
                minsteps = min(minsteps, jump)
        dp[i] = minsteps
    return dp[n-1]