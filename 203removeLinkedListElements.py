# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElementsRecursive(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
                
        if not head:
            return None
        
        head.next = self.removeElementsRecursive(head.next, val)

        if head.val == val:
            if head.next: 
                head.val = head.next.val
                head.next = head.next.next
            else:
                head = None
        
        return head


    def removeElementsIterative(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if not head:
            return
        
        cur = head
        
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        if head.val == val:
            head = head.next
        
        return head
