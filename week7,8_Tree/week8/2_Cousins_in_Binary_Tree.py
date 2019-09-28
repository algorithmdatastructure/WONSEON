# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Same depth, but different Parent -> True
Different depth -> False
Same Parent -> False

"""
#
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def dfs(node, parent, depth, target):
            if node :
                if node.val == target:
                    return depth, parent
                return dfs(node.left, node, depth+1, target) or dfs(node.right, node, depth+1, target)

        left_depth, left_parent = dfs(root, None, 0, x)
        right_depth, right_parent = dfs(root, None, 0, y)
        return left_depth == right_depth and left_parent != right_parent

#1.
# class Solution(object):
#     def isCousins(self, root, x, y):
#         """
#         :type root: TreeNode
#         :type x: int
#         :type y: int
#         :rtype: bool
#         """
#
#         head = root
#         left_val, left_count = dfs(head.left)
#         right_val, right_count = dfs(head.right)
#
#         def dfs(self, node):
#             ter = []
#             count = 0
#             if node:
#                 ter.append(node.val)
#                 coutn += 1
#                 dfs(node.left)
#                 dfs(node.right)
#             return ter[0], count
