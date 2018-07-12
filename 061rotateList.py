# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # calculate actual shift
        length = self.getLength(head)
        shift = k % length
        if shift == 0:
            return head
        
        # pick off the shifted numbers, stick them to the front
        cur = head
        for i in range(length - shift - 1): # this is actually shifting to the left, just changed the range
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        
        cur = newHead
        while cur.next:
            cur = cur.next
        
        cur.next = head
        
        return newHead
    
    
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length