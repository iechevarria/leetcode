# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        arr = self.recurse(root)
        return arr == sorted(arr) and len(arr) == len(set(arr))
    
    def recurse(self, root):
        l = r = []
        
        if root.left:
            l = self.recurse(root.left)
        if root.right:
            r = self.recurse(root.right)

        return l + [root.val] + r

class BetterSolution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.recurse(root, float('-inf'), float('inf'))
    
    def recurse(self, root, low, high):
        l = r = True
        if root.val <= low or root.val >= high:
            return False
        if root.left:
            l = self.recurse(root.left, low, root.val)
        if root.right:
            r = self.recurse(root.right, root.val, high)
        return l and r