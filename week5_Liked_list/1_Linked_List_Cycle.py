# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        memory = head

        while head and memory and memory.next:
            head = head.next
            memory = memory.next.next

            if head == memory:
                return True
        return False

# #----------------- Simple Solution
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         while head and head.val != None:
#             head.val, head = None, head.next
#         return head != None





if __name__ == '__main__':
    head = ListNode(3)
    new1 = ListNode(2)
    new2 = ListNode(0)
    new3 = ListNode(-4)

    head.next = new1
    new1.next = new2
    new2.next = new3
    new3.next = new1

    print(head.val)
    sol = Solution()
    # answer = Solution([3,2,0,-4])
    print(sol.hasCycle(head))
