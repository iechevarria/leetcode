"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        
        if not head:
            tmp = ListNode(insertVal)
            tmp.next = tmp
            return tmp
        
        length = self.getLength(head)

        cur = head
        for i in range(length):
            if insertVal >= cur.val and insertVal <= cur.next.val:
                self.insertAfter(cur, insertVal)
                return head
            cur = cur.next
            
        preMin = self.getMin(head, length)
        self.insertAfter(preMin, insertVal)
        return head
        
        
    def insertAfter(self, node, val):
        tmp = ListNode(val)
        tmp.next = node.next
        node.next = tmp
        
        
    def getLength(self, head):
        static = head
        walker = head.next
        
        length = 1
        
        while walker != static:
            walker = walker.next
            length += 1
        
        return length
        
        
    def getMin(self, head, length):
        preMin = head
        cur = head
        
        for i in range(length):
            if cur.next.val <=  preMin.next.val and cur.next.val < cur.next.next.val:
                preMin = cur
            cur = cur.next

        return preMin
            
            
                
        
        