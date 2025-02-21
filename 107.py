from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        levels = []
        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                level.append(root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            levels.append(level)
        return levels[::-1]
