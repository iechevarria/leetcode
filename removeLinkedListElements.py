# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
                
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)

        if head.val == val:
            if head.next: 
                head.val = head.next.val
                head.next = head.next.next
            else:
                head = None
        
        return head