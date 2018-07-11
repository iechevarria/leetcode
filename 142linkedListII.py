# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        slow = head
        fast = head
        
        slowTurn = False
        
        # check for a cycle
        while fast.next and slow.next:
            fast = fast.next
            if slowTurn:
                slow = slow.next
                slowTurn = False
            else:
                slowTurn = True
            if slow == fast:
                break
        
        if not fast.next:
            return None
        
        # get the length of the cycle
        cycleLength = 1
        fast = fast.next
        
        while fast != slow:
            fast = fast.next
            cycleLength += 1
            
        
        # get the first element
        fast = head
        slow = head
        
        for i in range(cycleLength):
            fast = fast.next
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return fast
            