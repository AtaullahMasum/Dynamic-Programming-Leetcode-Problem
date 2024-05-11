# using Recursion
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

from typing import List
def helper(ind, tar, arr):
    if ind == 0:
        if tar == 0 and arr[0] == 0:
            return 2
        if tar == 0 or tar == arr[0]:
            return 1
        return 0
    
    not_taken = helper(ind - 1, tar, arr)
    taken = 0
    if arr[ind] <= tar:
        taken = helper(ind-1, tar - arr[ind], arr)
    return  (not_taken+ taken)%(10**9 + 7)

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    totalSum = sum(arr)
    if totalSum - d < 0 or (totalSum -d)%2 :
        return 0
    tar = (totalSum -d )//2
    return helper(n-1, tar, arr)

# Using Memoization
# Time Complexity is O(n*k)
# Space Complexity is O(n*k) + O(n)
from os import *
from sys import *
from collections import *
from math import *

from typing import List
def helper(ind, tar, arr, dp):
    if ind == 0:
        if tar == 0 and arr[0] == 0:
            return 2
        if tar == 0 or tar == arr[0]:
            return 1
        return 0
    if dp[ind][tar] != -1:
        return dp[ind][tar]
    not_taken = helper(ind - 1, tar, arr, dp)
    taken = 0
    if arr[ind] <= tar:
        taken = helper(ind-1, tar - arr[ind], arr, dp)
    dp[ind][tar] = (not_taken+ taken)%(10**9 + 7)
    return dp[ind][tar]


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    totalSum = sum(arr)
    if totalSum - d < 0 or (totalSum -d)%2 :
        return 0
    tar = (totalSum -d )//2
    dp = [[-1]*(tar + 1) for _ in range(n)]
    return helper(n-1, tar, arr, dp )

# Using Tabulation Method 
# Time Complexity is O(n*k)
# Space Complexity is O(n*k)
from os import *
from sys import *
from collections import *
from math import *

from typing import List
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    totalSum = sum(arr)
    if totalSum - d < 0 or (totalSum -d)%2 :
        return 0
    tar = (totalSum -d )//2
    dp = [[0]*(tar + 1) for _ in range(n)]
    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
    if arr[0] != 0 and arr[0] <= tar:
        dp[0][arr[0]] = 1
    for i in range(1, n):
        for target in range(tar+1):
            not_taken = dp[i-1][target]
            taken = 0
            if arr[i] <= target:
                taken = dp[i-1][target - arr[i]]
            dp[i][target] = (not_taken + taken) % (10**9 + 7)
        
    return  dp[n-1][tar]
# Space Optimization 
# Time Complexity is O(n*k)
# Space Complexity is O(k)
from os import *
from sys import *
from collections import *
from math import *

from typing import List
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    totalSum = sum(arr)
    if totalSum - d < 0 or (totalSum -d)%2 :
        return 0
    tar = (totalSum -d )//2
    prev = [0]*(tar+1)
    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1
    if arr[0] != 0 and arr[0] <= tar:
        prev[arr[0]] = 1
    for i in range(1, n):
        curr = [0]*(tar+1)
        curr[0] =1
        for target in range(tar+1):
            not_taken = prev[target]
            taken = 0
            if arr[i] <= target:
                taken =prev[target - arr[i]]
            curr[target] = (not_taken + taken) % (10**9 + 7)
        prev = curr

    return  prev[tar]

    