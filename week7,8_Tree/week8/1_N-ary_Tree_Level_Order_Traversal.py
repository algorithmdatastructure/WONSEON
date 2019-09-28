"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 1
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        Q = [root]
        ret = []

        while any(Q):
            ret.append([node.val for node in Q])
            Q = [ child for node in Q for child in node.children]
        return ret

# 2
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        Q = deque([root])
        ret = []
        while Q:
            level = []
            for i in range(len(Q)):
                cur = Q.pop()
                for c in cur.children:
                    Q.appendleft(c)
                level.append(cur.val)
            ret.append(level)
        return ret
