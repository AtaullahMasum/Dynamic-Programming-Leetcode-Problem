# Using Recursion
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *
def helper(index, target, arr, dp):
    if target == 0:
        return True
    if index == 0:
        return arr[0] == target
    not_take = helper(index-1, target, arr, dp)
    take = False
    if target >= arr[index]:
        take = helper(index-1, target-arr[index], arr, dp)
    return not_take or take


def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return helper(n-1, k, arr, dp)
# Using Memoization
# Time Complexity is O(n*k)
# Space Complexity is O(n*k)
from os import *
from sys import *
from collections import *
from math import *
def helper(index, target, arr, dp):
    if target == 0:
        return True
    if index == 0:
        return arr[0] == target
    if dp[index][target] != -1:
        return dp[index][target]
    not_take = helper(index-1, target, arr, dp)
    take = False
    if target >= arr[index]:
        take = helper(index-1, target-arr[index], arr, dp)
    dp[index][target] = not_take or take
    return dp[index][target]


def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[-1]*(k+1) for _ in range(n)]
    return helper(n-1, k, arr, dp)
# Using tabulation Method
# Time Complexity is O(n*target)
# Space Complexity is O(n*target)
from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[False]*(k+1) for _ in range(n)]
    for ind in range(n):
        dp[ind][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True
    for ind in range(1, n):
        for target in range(1, k+1):
            not_taken = dp[ind-1][target]
            taken = False
            if arr[ind] <= target:
                taken = dp[ind-1][target - arr[ind]]
            dp[ind][target] = taken or not_taken
    return dp[n-1][k]