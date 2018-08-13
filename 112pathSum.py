# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.recurse(root, total, 0)
            
    def recurse(self, node, total, cur):
        if node is None:
            return False
        cur += node.val
        if node.left is None and node.right is None:
            return True if cur == total else False
        else:
            return self.recurse(node.left, total, cur) or self.recurse(node.right, total, cur)
