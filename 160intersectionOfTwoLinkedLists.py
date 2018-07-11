# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if (not headA) or (not headB):
            return None
        
        # find the lengths of the lists
        curA = headA
        curB = headB
        
        lenA = 0
        lenB = 0
        
        while curA:
            lenA += 1
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next
            
            
        # use the difference between the lists to align the tails, find the intersection
        curA = headA
        curB = headB
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        else:
            for i in range(lenB - lenA):
                curB = curB.next
                
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        
        return None
                
            
        
        