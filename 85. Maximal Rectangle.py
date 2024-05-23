# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]]>=heights[i]):
                height = heights[stack[-1]]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height*width)
            stack.append(i)
        return maxArea
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n , m = len(matrix), len(matrix[0])
        maxArea = 0
        heights = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea( heights)
            maxArea = max(maxArea, area)
        return maxArea
            