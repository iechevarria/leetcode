# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetricIterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root: return True
        
        queue = [root]
        
        while len(queue) > 0:
            tmp = []
            
            for i in range(len(queue)):
                tmp.append(queue.pop())
            
            for i in range(len(tmp)):
                if tmp[i]:
                    queue.append(tmp[i].left)
                if tmp[i]:
                    queue.append(tmp[i].right)
            
            for i in range(len(tmp)):
                if tmp[i]: tmp[i] = tmp[i].val

            if tmp != tmp[::-1]: return False
        
        return True
  

    def isSymmetricRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetry(root.left, root.right) if root else True
        
    def symmetry(self, r1, r2):
        if not r1 and not r2: return True
        elif not r1 or not r2: return False
        return self.symmetry(r1.left, r2.right) and self.symmetry(r1.right, r2.left) if r1.val == r2.val else False