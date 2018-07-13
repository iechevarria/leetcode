# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        tmp = []
        
        if not root:
            return tmp
        
        if root.left:
            tmp += self.postorderTraversal(root.left)
        if root.right:
            tmp += self.postorderTraversal(root.right)
        
        return tmp + [root.val]