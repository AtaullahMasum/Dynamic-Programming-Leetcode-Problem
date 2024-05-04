# Brute Force Solution 
# Time Complexity is O(2^(m+n))
# Space Complexity is O((m-1)+(n-1))
from collections import *
from math import *
def helper(row, col):
	if row == 0 and col == 0:
		return 1
	if row < 0 or col < 0:
		return 0
	up = helper(row-1, col)
	left = helper(row, col-1)
	return up + left
def uniquePaths(m, n):
	# Write your code here.
	return helper(m-1, n-1)
# Using Memoization 
# Time Complexity is O(m*n)
# Space complexity is O((m-1)+(n-1)) + O(n*m)
from collections import *
from math import *
def helper(row, col, dp):
	if row == 0 and col == 0:
		return 1
	if row < 0 or col < 0:
		return 0
	if dp[row][col] != -1:
		return dp[row][col]
	up = helper(row-1, col, dp)
	left = helper(row, col-1, dp)
	dp[row][col] = up + left
	return dp[row][col]
def uniquePaths(m, n):
	# Write your code here.
	dp = [[-1]*n for _ in range(m)]
	return helper(m-1, n-1, dp)
# Tabulation method
# Time Complexity is O(m*n)
# Space Complexity is O(m*n)
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
	dp = [[0]*n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			if i == 0 and j == 0:
				dp[i][j] = 1
			else:
				up , left = 0,0
				if i > 0:
					up = dp[i-1][j]
				if j > 0:
					left = dp[i][j-1]
				dp[i][j] = up + left
	return dp[-1][-1]