# Using Recursion Method
# Time Complexity is Exponential 
# Space Complexity is O(n)
class Solution:
    def isPalindrome(self,start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def findPalindrome(self, i, s):
        if i == len(s):
            return 0
        minCost = float('inf')
        for j in range(i, len(s)):
            if self.isPalindrome(i, j, s):
                cost = 1 + self.findPalindrome(j+1, s)
                minCost = min(minCost, cost)
        return minCost
                
    def minCut(self, s: str) -> int:
        return self.findPalindrome(0, s) - 1
# Using Memoization Method
# Time Complexity is O(n^2)
# Space Complexity is O(n) + O(n)
class Solution:
    def isPalindrome(self,start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def findPalindrome(self, i, s, dp):
        if i == len(s):
            return 0
        if dp[i] != -1:
            return dp[i]
        minCost = float('inf')
        for j in range(i, len(s)):
            if self.isPalindrome(i, j, s):
                cost = 1 + self.findPalindrome(j+1, s, dp)
                minCost = min(minCost, cost)
        dp[i] = minCost
        return dp[i]
                
    def minCut(self, s: str) -> int:
        dp = [-1]*len(s)
        return self.findPalindrome(0, s, dp) - 1
# Using Tabulation Method
# Time Complexity is O(n^2)
# Space Complexity is O(n)
class Solution:
    def isPalindrome(self,start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
                
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            minCost = float('inf')
            for j in range(i, len(s)):
                if self.isPalindrome(i,j,s):
                    cost = 1 + dp[j+1]
                    minCost = min(minCost, cost)
            dp[i] = minCost
        return dp[0]-1
# Above all these code has TLE issue some cases
# Bellow the Solution is correct
class Solution:            
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[True]*n for i in range(n)]
        result = [-1] + [float("inf")]*n
        for i in range(n):
            for j in range(i+1):
                palindrome[j][i] = (s[j] == s[i] and (i-j <= 2 or palindrome[j+1][i-1]))
                if palindrome[j][i]:
                    result[i+1] = min(result[i+1], result[j]+1)
        return result[n]

