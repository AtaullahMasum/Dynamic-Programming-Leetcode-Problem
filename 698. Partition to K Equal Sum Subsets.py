# Using Backtracking 
# Time Complexity is O(nlogn + 2^n.k)
# Space Complexity is O(n)
class Solution:
    def helper(self, start_index, current_sum, target, nums, remaining_subsets, visited):
        if remaining_subsets == 0:
            return True
        if current_sum == target:
            return self.helper(0,0, target, nums, remaining_subsets - 1, visited)
        for i in range(start_index, len(nums)):
            if visited[i] or current_sum + nums[i] > target:
                continue
            if not visited[i] and current_sum + nums[i] <= target:
                visited[i] = True
                if self.helper(i+1, current_sum + nums[i], target, nums, remaining_subsets, visited):
                    return True
                visited[i] = False
            # Early pruning
            if current_sum == 0 or current_sum + nums[i] == target:
                    break        
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        if total_sum%k != 0:
            return False
        target = total_sum//k
        visited = [False]*len(nums)
        return self.helper( 0, 0, target, nums, k, visited)
        