# Space Optimazation Solution
# Time Complexity is O(2n)
# Space Complexity is O(1)
class Solution:
    def robHouse1(self, nums):
        prev = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2
            non_take = 0 + prev
            curri = max(take, non_take)
            prev2 = prev
            prev = curri
        return prev
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans1 = self.robHouse1(nums[1:])
        ans2 = self.robHouse1(nums[:-1])
        return max(ans1, ans2 )