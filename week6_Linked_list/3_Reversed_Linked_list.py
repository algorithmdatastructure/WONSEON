# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" Approach 1 : Iteratively """
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



""" Approach 2 : Recursively """
# class Solution:
#     def reverseList(self, head: ListNode, prev=None) -> ListNode: # input type과 -> return type
#         if head is None:
#             return prev
#
#         cur, head.next = head.next, prev
#         return self.reverseList(cur, prev=head)

    # def reverseList(self, head: ListNode, prev=None) -> ListNode: # input type과 -> return type
    #     if head is None or head.next is None:
    #         return head
    #     p = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return p



if __name__ == "__main__" :
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)

    b = Solution().reverseList(a)

    while b :
        print(b.val)
        b = b.next
