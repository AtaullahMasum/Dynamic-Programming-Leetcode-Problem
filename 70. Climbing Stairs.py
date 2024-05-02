# using fibonacci number
# Time Complexity is O(n)
# Space Complexity is O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev = 1
        for i in range(2, n+1):
            curr = prev1 + prev
            prev1 = prev
            prev = curr
        return prev