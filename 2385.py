from collections import deque
from typing import Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def markParents(self, root: TreeNode, parents: Dict[TreeNode, TreeNode]):
        if not root:
            return

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parents[node.left] = node
                q.append(node.left)
            if node.right:
                parents[node.right] = node
                q.append(node.right)


    def findNode(self, root: Optional[TreeNode], node: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == node:
            return root

        return self.findNode(root.left, node) or self.findNode(root.right, node)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        startNode = self.findNode(root, start)
        parents = {}
        self.markParents(root, parents)
        parents[root] = None

        visited = set()
        q = deque([startNode])
        visited.add(startNode)

        time = 0
        while q:
            for i in range(len(q)):
                root = q.popleft()

                if root.left and not root.left in visited:
                    visited.add(root.left)
                    q.append(root.left)

                if root.right and not root.right in visited:
                    visited.add(root.right)
                    q.append(root.right)

                if parents[root] and parents[root] not in visited:
                    visited.add(parents[root])
                    q.append(parents[root])
            time += 1

        return time-1