# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            nonlocal diff
            diff = max(diff, abs(lh - rh))
            return 1 + max(lh, rh)
        height(root)
        return diff <= 1