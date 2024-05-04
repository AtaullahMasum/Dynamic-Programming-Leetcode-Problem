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
# Time Complexity is O(n*4*3)
# Space COmplexity is O(n*4)+O(n)
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
# Using Tabulation method
# Time Complexity is O(n*4*3)
# Space Complexity is O(n*4)
from typing import *
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1] * 4 for _ in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], point)
    return dp[n-1][3]
# Tabulation to space Optimazation
# Time Complexity is O(n*4*3)
# Space Complexity is O(4)+ O(4)
from typing import *
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [0]*4
    dp[0] = max(points[0][1], points[0][2])
    dp[1] = max(points[0][0], points[0][2])
    dp[2] = max(points[0][0], points[0][1])
    dp[3] = max(points[0][0], points[0][1], points[0][2])
    for day in range(1, n):
        temp = [0]*4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task != last:
                    temp[last] = max(temp[last],  points[day][task] + dp[task])
        dp = temp
    return dp[3]
    
    
