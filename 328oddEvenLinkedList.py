# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next or not head.next.next:
            return head
    
        oddEnding = head
        cur = head.next
        count = 0
        while cur and cur.next:
            tmp = ListNode(cur.next.val)
            tmp.next = oddEnding.next
            oddEnding.next = tmp
            oddEnding = tmp
            cur.next = cur.next.next
            cur = cur.next
        
        return head