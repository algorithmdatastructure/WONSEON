
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#PEP 3107 -- Function Annotations
class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode: # input type과 -> return type
        if head is None:
            return prev

        cur, head.next = head.next, prev
        return self.reverseList(cur, prev=head)


    def printList(self):
        temp = self.head
        while(temp):
            print (temp.val)
            temp = temp.next




if __name__ == "__main__":

    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)

    x1.next = x2
    x2.next = x3

    sol = Solution()
    
