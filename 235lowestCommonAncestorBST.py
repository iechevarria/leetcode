# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        cur = root

        while cur:
            if cur.val == p.val:
                return p
            elif cur.val == q.val:
                return q
            elif cur.val < q.val and cur.val < p.val:
                cur = cur.right
            elif cur.val > q.val and cur.val > p.val:
                cur = cur.left
            else:
                return cur
            
class ImprovedSolution(object):
    def lowestCommonAncestor(self, r, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        while r:
            if r.val < q.val and r.val < p.val:
                r = r.right
            elif r.val > q.val and r.val > p.val:
                r = r.left
            elif r.val == p.val:
                return p
            elif r.val == q.val:
                return q
            else:
                return r
