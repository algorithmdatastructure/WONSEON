# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" Approach 1 : Traverse list Once, get size"""
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        head_length = 0
        while temp:
            head_length += 1
            temp = temp.next

        middle = head_length / 2

        for i in range(middle):
            head = head.next

        return head

""" Approach 2 : Fast & Slow Pointer(Trick) """
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        return slow
