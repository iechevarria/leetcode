class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return s[::-1]

    def reverseStringAlt(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp
        
        return ''.join(s)