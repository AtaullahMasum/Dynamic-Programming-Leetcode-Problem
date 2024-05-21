# Using Two Pointer and Sliding Window 
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def longestMountain(self, nums: List[int]) -> int: 
        if len(nums)<3:
            return 0
        n = len(nums)
        longest = 0
        i = 1
        while i < n-1:
            if nums[i-1] < nums[i] > nums[i+1]:
                left = i-1
                while left > 0 and nums[left-1] < nums[left]:
                    left -= 1
                right = i+1
                while right < n-1 and nums[right] > nums[right + 1]:
                    right += 1
                current_length = right - left + 1
                longest = max(longest, current_length)
                i = right
            else:
                i += 1
        return longest