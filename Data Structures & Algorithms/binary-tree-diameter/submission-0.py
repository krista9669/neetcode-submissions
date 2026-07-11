# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(
            self.max_depth(root.left),
            self.max_depth(root.right)
        )
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)
        current = left_height + right_height
        left_ = self.diameterOfBinaryTree(root.left)
        right_ = self.diameterOfBinaryTree(root.right)
        return max(current,left_,right_)