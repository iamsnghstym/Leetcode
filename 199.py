from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_view = []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                level.insert(0, root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            right_view.append(level[0])
        return right_view
