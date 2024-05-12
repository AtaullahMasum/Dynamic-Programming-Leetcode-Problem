# Using Recursion
# Time Complexity is O(2^n)
# Space Complexity is O(n)
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def helper(ind, W,  wt, val):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    not_peak = 0+ helper(ind-1, W, wt, val)
    peak = float('-inf')
    if wt[ind] <= W:
        peak = val[ind] + helper(ind-1, W-wt[ind], wt, val)
    return max(not_peak, peak)
def knapsack(wt, val, W, n):
    return helper(n-1, W, wt, val)

T = int(input())
for i in range(T):
    n = int(input())
    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))
    W = int(input())
    if len(wt) != n or len(val) !=n:
        print("Error")
        continue
    print(knapsack(wt, val, W, n))
# Using Memoization 
# Time Complexity is O(n*w)
# Space Complexity is O(n*w) + O(n)
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def helper(ind, W,  wt, val, dp):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    if dp[ind][W] != -1:
        return dp[ind][W]
    not_peak = 0+ helper(ind-1, W, wt, val, dp)
    peak = float('-inf')
    if wt[ind] <= W:
        peak = val[ind] + helper(ind-1, W-wt[ind], wt, val, dp)
    dp[ind][W] = max(not_peak, peak)
    return dp[ind][W]
def knapsack(wt, val, W, n):
    dp = [[-1]*(W+1) for _ in range(n)]
    return helper(n-1, W, wt, val, dp)

T = int(input())
for i in range(T):
    n = int(input())
    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))
    W = int(input())
    if len(wt) != n or len(val) !=n:
        print("Error")
        continue
    print(knapsack(wt, val, W, n))
# Using Tabulation Method 
# Time Complexity is O(n*w)
# Space Complexity is O(n*w)
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack(wt, val, W, n):
    dp = [[0]*(W+1) for _ in range(n)]
    for weight in range(wt[0], W+1):
        dp[0][weight] = val[0]
    for i in range(1, n):
        for weight in range( W+1):
            not_take = dp[i-1][weight]
            take = float('-inf')
            if wt[i] <= weight:
                take = val[i] + dp[i-1][weight - wt[i]]
            dp[i][weight] = max(not_take, take)
    return dp[n-1][W]
   

T = int(input())
for i in range(T):
    n = int(input())
    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))
    W = int(input())
    if len(wt) != n or len(val) !=n:
        print("Error")
        continue
    print(knapsack(wt, val, W, n))
    
# Using Space Optimization Method 
# Time Complexity is O(n*w)
# Space Complexity is O(w)
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack(wt, val, W, n):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for w in range(wt[0], W + 1):
        if wt[0] <= W:
            prev[w] = val[0]

    for i in range(1, n):
        for w in range(W + 1):
            include = 0
            if wt[i] <= w:
                include = val[i] + prev[w - wt[i]]
            exclude = prev[w]
            curr[w] = max(include, exclude)
        prev = curr[:]

    return prev[W]

T = int(input())
for i in range(T):
    n = int(input())
    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))
    W = int(input())
    if len(wt) != n or len(val) !=n:
        print("Error")
        continue
    print(knapsack(wt, val, W, n))
# Space Optimization Using Single Row
# Time Complexity is O(n*w)
# Space Complexity is O(w)
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack(wt, val, W, n):
    prev = [0] * (W + 1)

    for w in range(wt[0], W + 1):
        if wt[0] <= W:
            prev[w] = val[0]

    for i in range(1, n):
        for w in range(W , -1, -1):
            include = 0
            if wt[i] <= w:
                include = val[i] + prev[w - wt[i]]
            exclude = prev[w]
            prev[w] = max(include, exclude)

    return prev[W]

T = int(input())
for i in range(T):
    n = int(input())
    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))
    W = int(input())
    if len(wt) != n or len(val) !=n:
        print("Error")
        continue
    print(knapsack(wt, val, W, n))

