# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return False
        
        slow = head
        fast = head
        
        slowturn = False
        
        while slow.next and fast.next:
            if slowturn:
                slow = slow.next
                slowturn = False
            else:
                slowturn = True
            fast = fast.next
            
            if fast == slow:
                return True
        
        return False
            