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


    def longestCommonPrefixAlt(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
                
        commonPrefix= ""
        
        if len(strs) < 1 or "" in strs:
            return commonPrefix

        i = 0
        
        while True:
            try:
                s = strs[0][i]
            except IndexError:
                return commonPrefix
            for string in strs:
                try:
                    if string[i] != s:
                        return commonPrefix
                except IndexError:
                    return commonPrefix
            commonPrefix += s
            i += 1