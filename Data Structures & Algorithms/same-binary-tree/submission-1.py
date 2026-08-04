# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        if not q:
            return not p

        if p.val == q.val:
            is_left_same = self.isSameTree(p.left, q.left)
            is_right_same = self.isSameTree(p.right, q.right)
        else:
            return False
        return is_left_same and is_right_same

        