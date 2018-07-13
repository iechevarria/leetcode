# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        tmp = [root.val]
        if root.left:
            tmp += self.preorderTraversal(root.left)
        if root.right:
            tmp += self.preorderTraversal(root.right)
            
        return tmp