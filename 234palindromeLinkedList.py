# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        if not head:
            return 0
        
        count = 0
        while head:
            head = head.next
            count += 1
        
        return count
    
    
    def reverseList(self, head):
        if not head:
            return None
    
        front = head
        
        while head.next:
            tmp = ListNode(head.next.val)
            tmp.next = front
            front = tmp
            head.next = head.next.next
        
        return front
            
    
    def isPalindrome(self, head):
        length = self.getLength(head)
        
        curA = head
        curB = head
        
        for i in range(math.ceil(length / 2)):
            curA = curA.next
        
        curA = self.reverseList(curA)
        while curA:
            if curA.val != curB.val:
                return False
            curA = curA.next
            curB = curB.next
        
        return True
        
        
    def isPalindromeLazy(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return True
        
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
        
        return vals == vals[::-1]
