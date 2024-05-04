# Using recursion
# Time Complexity is O(n^3)
# Space Complexity is O(n)
from typing import *
def helper(day, last, points):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    maxi = 0
    for task in range(3):
        if task != last:
            point = points[day][task] + helper(day-1, task, points)
            maxi = max(maxi, point)
    return maxi

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1] * 4 for _ in range(n)]  
    return helper(n-1, 3, points)
    


# Using Memoization
# Time Complexity is O(n)
# Space COmplexity is O(n*4)
from typing import *
def helper(day, last, points, dp):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        dp[day][last] = maxi
        return dp[day][last]
    if dp[day][last] != -1:
        return dp[day][last]
    maxi = 0
    for task in range(3):
        if task != last:
            point = points[day][task] + helper(day-1, task, points, dp)
            maxi = max(maxi, point)
    dp[day][last] = maxi
    
    return dp[day][last]

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1] * 4 for _ in range(n)]  
    return helper(n-1, 3, points, dp)
    
