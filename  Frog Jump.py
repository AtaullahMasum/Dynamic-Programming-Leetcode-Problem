# Solution one using simple recursion
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

from typing import *
def f(index, heights):
    if index == 0:
        return 0
   
    left = f(index-1, heights) + abs(heights[index]-heights[index-1])
    right = float('inf')
    if index > 1:
        right = f(index-2, heights) + abs(heights[index]- heights[index-2])
    return  min(left, right)
   
  
def frogJump(n: int, heights: List[int]) -> int:
    
    return f(n-1, heights)


# Solution two using memoization
# Time Complexity is O(n)
# Space Compexity is O(n) + O(n)
from os import *
from sys import *
from collections import *
from math import *

from typing import *
def f(index, heights, dp):
    if index == 0:
        return 0
    if dp[index] != -1:
        return dp[index]
    left = f(index-1, heights, dp) + abs(heights[index]-heights[index-1])
    right = float('inf')
    if index > 1:
        right = f(index-2, heights, dp) + abs(heights[index]- heights[index-2])
    dp[index] = min(left, right)
    return dp[index]
  
def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1]*(n+1)
    return f(n-1, heights, dp)

# Memoization convert into tabulation
# Time Complexity is O(n)
# Space Compexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp = [0]*n
    dp[0] = 0
    for i in range(1, n):
        fs = dp[i-1] +abs(heights[i] - heights[i-1])
        ss = float('inf')
        if i > 1:
            ss = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(fs, ss)
    return dp[n-1]

