class Solution:
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 1 if len(s) > 0 else 0         
      
        for i in range(len(s)):
            while not self.checkForDuplicates( s[i: i + maxLength + 1]) and maxLength + i < len(s): # I got very stupidly stuck here, string slice is extremely permissive and allowed me to go outside the string
                maxLength += 1
        
        return maxLength
            
    def checkForDuplicates(self, sub): # I spent more time optimizing this because I thought my problems were here
        """
        :type s: str
        :rtype: bool
        """
        count = {}
        for c in sub: 
            if c in count:
                return True
            else:
                count[c] = 1
        
        return False
      
