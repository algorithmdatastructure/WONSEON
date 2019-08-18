# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#PEP 3107 -- Function Annotations
class Solution:
    def __init__(self) :
        self.head = None
        # self.cur = None
        # self.prev = None

    def reverseList(self, head: ListNode) -> ListNode: # input type과 -> return type
        self.head = head
        prev = None
        cur = self.head

        while cur != None :
            after = cur.next
            cur.next = prev
            prev = cur
            cur = cur.next
        self.head = prev

        return self.head

    def push(self, new_data):
        new_node = ListNode(new_data) 
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next


if __name__ == "__main__":

    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)

    x1.next = x2
    x2.next = x3

    sol = Solution()

    print(sol.reverseList(x1))
