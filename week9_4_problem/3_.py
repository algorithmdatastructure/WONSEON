# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        result = []

        if root.left is not None:
            result = result + self.increasingBST(root.left)

        result = result.append(root.val)

        if root.right is not None:
            result = result + self.increasingBST(root.right)

        return result
