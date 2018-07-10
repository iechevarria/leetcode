class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        longest = ""
        
        if len(strs) < 1:
            return longest
        
        length = len(min(strs, key=len))
        
        for i in range(length):
            candidate = strs[0][0:i+1]
            for j in range(len(strs)):
                if strs[j][0:i+1] != candidate:
                    return longest
            longest = candidate
        
        return longest
                