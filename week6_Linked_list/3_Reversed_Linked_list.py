# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

""" Approach 1 : Iteratively """
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse_list = ListNode(head.val)
        while head.next:
            head = head.next
            newNode = ListNode(head.val)
            newNode.next = reverse_list
            reverse_list = newNode
        return reverse_list



""" Approach 2 : Recursively """
