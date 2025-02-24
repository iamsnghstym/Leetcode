from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        return True if abs(lheight-rheight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) else False

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
