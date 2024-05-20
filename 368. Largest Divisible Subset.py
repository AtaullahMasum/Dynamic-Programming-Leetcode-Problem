# Using Tabulation Method
# Time Complexity is O(n*n)
# Space Complexity is O(n) + O(n)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        hashMap = [0]*n
        dp = [1]*n
        lastIndex = 0
        maxi = 1
        for i in range(n):
            hashMap[i] = i
            for prev in range(i):
                if nums[i]% nums[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1+dp[prev]
                    hashMap[i] = prev
            if maxi < dp[i]:
                maxi = dp[i]
                lastIndex = i
        temp = []
        temp.append(nums[lastIndex])
        while hashMap[lastIndex] != lastIndex:
            lastIndex = hashMap[lastIndex]
            temp.append(nums[lastIndex])
        return temp[::-1]