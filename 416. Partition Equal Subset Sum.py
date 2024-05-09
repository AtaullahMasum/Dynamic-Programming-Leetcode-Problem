# These problem same as Subset Sum Equal to K in these repository
#https://github.com/AtaullahMasum/Dynamic-Programming-Leetcode-Problem/blob/master/Subset%20Sum%20Equal%20To%20K.py
# Space Optimazation SOlution Added
class Solution:
    def subsetSumToK(self, n, k, arr):
        prev = [False]*(k+1)
        prev[0] = True  
        if arr[0] <= k:
            prev[arr[0]] = True
            
        for ind in range(1, n):
            curr = [False]*(k+1)
            curr [0] = True
            for target in range(1, k+1):
                not_taken = prev[target]
                taken = False
                if arr[ind] <= target:
                    taken = prev[target- arr[ind]]
                curr [target] = not_taken or taken
            prev = curr
        return prev[k]
 
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        if total_sum % 2:
            return False
        return self.subsetSumToK(len(nums), total_sum//2 , nums)