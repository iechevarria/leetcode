class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0
        
        nLen = len(needle)
        hLen = len(haystack)
        
        if nLen > hLen:
            return -1
        
        for i in range(hLen - nLen + 1):
            if haystack[i:i+nLen] == needle:
                return i
        
        return -1
