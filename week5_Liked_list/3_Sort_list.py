# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        temp2 = head
        py_list = []
        while temp:
            py_list.append(temp.val)
            temp = temp.next

        py_list.sort()
