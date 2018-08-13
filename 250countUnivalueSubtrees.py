# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recurse(root)[0]
        
    def recurse(self, node):
        if node is None:
            return [0, 1]
        l = self.recurse(node.left)
        r = self.recurse(node.right)
        if (l[1] == 1 and r[1] == 1) and (node.left is None or node.left.val == node.val) and (node.right is None or node.right.val == node.val):
            return [1+l[0]+r[0], 1]
        else:
            return [l[0]+r[0], 0]