# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # solved by finding the max sum of depth of both sides of any particular root
        if not root:
            return 0
        diam = 0
        def height(node: Optional[TreeNode]) -> int:
            nonlocal diam
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            diam = max(diam, left_h + right_h)
            return 1 + max(left_h, right_h)
        
        height(root)
        return diam
        