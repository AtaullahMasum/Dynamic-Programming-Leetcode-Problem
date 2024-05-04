# Brute force Solution 
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
def helper(index, nums):
    if index == 0:
        return nums[index]
    if index < 0:
        return 0
    peak = nums[index] + helper(index-2, nums)
    not_peak = 0 + helper(index-1, nums)
    return max(peak, not_peak)

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    
    return helper(len(nums)-1, nums)
    

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
# Using Memoization
# Time Complexity is O(n)
# Space Complexity is O(n)+O(n)
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
def helper(index, nums):
    if index == 0:
        return nums[index]
    if index < 0:
        return 0
    peak = nums[index] + helper(index-2, nums)
    not_peak = 0 + helper(index-1, nums)
    return max(peak, not_peak)

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    
    return helper(len(nums)-1, nums)
    

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
# Using Tabulation
# Time Complexity is O(n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp = [0]*(len(nums))
    dp[0] = nums[0]
    neg = 0
    for i in range(1, len(nums)):
        take = nums[i]
        if i > 1:
            take += dp[i-2]
        non_take = 0 + dp[i-1]
        dp[i] = max(take, non_take)
    return dp[len(nums)-1]

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
# Using Space Optimization
# Time Complexity is O(n)
# Space Complexity is O(1)
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


def maximumNonAdjacentSum(nums):    
    # Write your code here.
   
    prev = nums[0]
    prev2 = 0
    for i in range(1, len(nums)):
        take = nums[i] + prev2
        non_take = 0 + prev
        curri = max(take, non_take)
        prev2 = prev
        prev = curri
    return prev
# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
# Leetcode problem : 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            take = nums[i] + prev2
            non_take = 0 + prev
            curri = max(take, non_take)
            prev2 = prev
            prev = curri
        return prev
        