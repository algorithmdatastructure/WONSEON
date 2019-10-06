# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(node, parent, depth, target):
            if node :
                if node.val == target:
                    return depth, parent
                return dfs(node.left, node, depth+1, target) or dfs(node.right, node, depth+1, target)

        return 
