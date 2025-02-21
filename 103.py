from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        q = deque([root])
        direction = True
        """
            direction => True (Left -> Right)
                      => False (Right -> Left)
        """
        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                if direction:
                    level.append(root.val)
                else:
                    level.insert(0, root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            levels.append(level)
            direction = not direction
        return levels