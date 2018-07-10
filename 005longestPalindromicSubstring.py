class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        longest = ""
        b = 0 # offset from root of palindrome

        # even case
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                while self.isPalindrome(s[i-b: i+b+2]) and i-b >= 0 and i+b+2 <= len(s): # leqs instead of simple less thans here
                    longest = s[i-b:i+b+2]
                    b += 1
      
        # odd case
        for i in range(len(s)):
            while self.isPalindrome(s[i-b:i+b+1]) and i-b >= 0 and i+b+1 <= len(s):
                longest= s[i-b:i+b+1]
                b += 1
        
        return longest    
    
    
    def isPalindrome(self, s):
        if len(s) <= 1: # had the inequality going the wrong way here
            return True
        
        ptr1 = 0
        ptr2 = len(s) - 1
        
        while ptr1 < ptr2:
            if s[ptr1] != s[ptr2]: # made a stupid mistake here
                return False
            ptr1 += 1
            ptr2 -= 1
        
        return True