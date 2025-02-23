# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, lroot: Optional[TreeNode], rroot: Optional[TreeNode]):
        if not lroot and not rroot:
            return True
        if not lroot or not rroot:
            return False

        if lroot.val != rroot.val:
            return False

        return True if self.checkSymmetry(lroot.left, rroot.right) and self.checkSymmetry(lroot.right, rroot.left) else False

        