# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val < l2.val:
            l = l1
        else:
            l = l2

        while l1.next or l2.next :
            if l1.next.val <= l2.next.val :
                l.next = l1.next
                l1 = l1.next
            else :
                l.next = l2.next
                l2 = l2.next



        return l
