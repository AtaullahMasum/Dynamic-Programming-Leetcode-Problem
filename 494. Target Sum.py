# Using Memoization 
# Time Complexity is O(n*target)
# Space Complexity is (n*target)+ O(n)
class Solution:
    def helper(self,ind, tar, arr, dp):
        if ind == 0:
            if tar == 0 and arr[0] == 0:
                return 2
            if tar == 0 or tar == arr[0]:
                return 1
            return 0
        if (ind,tar) in dp:
            return dp[(ind, tar)]
        not_taken = self.helper(ind - 1, tar, arr, dp)
        taken = 0
        if arr[ind] <= tar:
            taken = self.helper(ind-1, tar - arr[ind], arr, dp)
        dp[(ind, tar)] = (not_taken+ taken)
        return dp[(ind, tar)]

    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        # write your code here
        totalSum = sum(arr)
        if totalSum - d < 0 or (totalSum -d)%2 :
            return 0
        tar = (totalSum -d )//2
        dp = {}
        return self.helper(n-1, tar, arr, dp )
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.countPartitions(len(nums), target, nums)
        