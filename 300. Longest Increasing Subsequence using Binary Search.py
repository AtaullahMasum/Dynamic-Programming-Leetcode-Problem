class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                length += 1
            else:
                ind = bisect_left(temp, nums[i])
                temp[ind] = nums[i]
        return length