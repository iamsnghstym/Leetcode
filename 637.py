from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            levels.append(sum(level)/len(level))
        return levels
