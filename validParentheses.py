class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        d = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        s = list(s)
        stack = []
        
        for i in range(len(s)):
            paren = s.pop(0)
            if paren not in d:
                stack.append(paren)
            elif len(stack) == 0 or stack.pop() != d[paren]:
                return False
        
        if len(stack) > 0:
            return False
        
        return True