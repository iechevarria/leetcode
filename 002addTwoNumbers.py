# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(l1.val + l2.val)

        if root.val > 9: # repeated code below
            root.val -= 10
            carry = 1
        else:
            carry = 0
        
        l1 = l1.next
        l2 = l2.next

        cur = root

        while (l1 is not None) or (l2 is not None):
            if (l1 is None):
                toAppend = ListNode(l2.val + carry)
                l2 = l2.next
            elif (l2 is None):
                toAppend = ListNode(l1.val + carry)
                l1 = l1.next
            else:
                toAppend = ListNode(l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next
                
            if toAppend.val > 9:
                toAppend.val -= 10
                carry = 1
            else:
                carry = 0
                
            cur.next = toAppend
            cur = cur.next
        
        if carry > 0: # I got this wrong on the first attempt
            cur.next = ListNode(carry)
        
        return root

  