from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildBST(self, nums: List[int], low: int, high: int):
        if low > high:
            return None

        mid = (low + high)//2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, low, mid-1)
        root.right = self.buildBST(nums, mid+1, high)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        low, high = 0, len(nums)-1
        return self.buildBST(nums, low, high)


# Approach -2 (slicing takes extra memory and time)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        low, high = 0, len(nums)-1
        mid = low+(high-low)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root