# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return []
        
        queue = [root]
        level = 0
        res = []
                
        while len(queue) > 0:
            tmp = []
            for i in range(len(queue)):
                tmp.append(queue.pop(0))
                
            for j in range(len(tmp)):
                if tmp[j].left:
                    queue.append(tmp[j].left)
                if tmp[j].right:
                    queue.append(tmp[j].right)
            
            res.append([x.val for x in tmp])
            level += 1
        
        return res
        