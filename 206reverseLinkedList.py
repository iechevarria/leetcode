# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        front = head
        
        while head.next:
            tmp = ListNode(head.next.val)
            tmp.next = front # got held up on this line, was using head before
            front = tmp
            head.next = head.next.next
        
        return front