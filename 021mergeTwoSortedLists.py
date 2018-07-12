# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        root = ListNode(0) # also got stuck here, good trick to know
        cur = root
        
        while l1 or l2:
            if l1 and not l2:
                cur.next = l1
                l1 = None # didn't have this before and got a bit stuck on it
            elif l2 and not l1:
                cur.next = l2
                l2 = None
            else:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = cur.next
                    l2 = l2.next
        
        return root.next


    def mergeTwoListsII(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(-1)
        cur = head
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        if not l1:
            cur.next = l2
        elif not l2:
            cur.next = l1
        
        return head.next