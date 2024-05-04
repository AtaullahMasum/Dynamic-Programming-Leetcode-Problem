# Brute Force Solution
# Time Complexity is O(N)
# Space Complexity is O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root):
        if not root:
            return 0, 0
        left_not_rob, left_rob = self.postorder(root.left)
        right_not_rob, right_rob = self.postorder(root.right)

        not_rob = max(left_not_rob, left_rob) + max(right_not_rob, right_rob)
        rob = root.val + left_not_rob + right_not_rob
        return (not_rob, rob)
    def rob(self, root: Optional[TreeNode]) -> int:
        not_rob , rob = self.postorder(root)
        return max(not_rob, rob)
# Same Code But Look more readable 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root):
        if not root:
            return [0, 0]
        leftPair = self.postorder(root.left)
        rightPair = self.postorder(root.right)

        robWithRoot = root.val + leftPair[1] + rightPair[1]
        robWithoutRoot = max(leftPair) + max(rightPair)
        return [robWithRoot, robWithoutRoot]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.postorder(root))
       