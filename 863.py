from collections import deque
from typing import Dict, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        self.markParents(root, parents)
        parents[root] = None

        visited = set()
        q = deque([target])
        visited.add(target)

        dist = 0
        while q:
            dist += 1
            if dist > k:
                break

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

        result = []
        while q:
            result.append(q.popleft().val)
        return result