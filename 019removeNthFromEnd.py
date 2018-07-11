# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
                
        front = head
        back = head
        
        for i in range(n):
            front = front.next
        
        if not front:
            head = head.next
            return head
        
        while front.next:
            front = front.next
            back = back.next
        
        back.next = back.next.next
        
        return head