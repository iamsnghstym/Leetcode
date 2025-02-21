from typing import  Optional, Dict
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getParent(self, root: Optional[TreeNode], parentMap: Dict[int, int]):
        q = deque([root])
        while q:
            root = q.popleft()
            if root.left:
                parentMap[root.left.val] = root.val
                q.append(root.left)
            if root.right:
                parentMap[root.right.val] = root.val
                q.append(root.right)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentMap = {}
        self.getParent(root, parentMap)

        print("parentMap - ", parentMap)
        q = deque([root])
        while q:
            """
                1. Cousins should be at the same level
                2. They should have different parents
            """
            seen = set()
            for i in range(len(q)):
                root = q.popleft()
                seen.add(root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)

                # If both x and y are at the same level
                if x in seen and y in seen:
                    # Check for parent
                    if parentMap[x] != parentMap[y]:
                        return True
                        
        return False

