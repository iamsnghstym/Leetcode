from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder, stack = [], []
        temp = []

        if not root:
            return postorder
        stack.append(root)
        while stack:
            root = stack.pop()
            temp.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        while temp:
            postorder.append(temp.pop())
        return postorder
