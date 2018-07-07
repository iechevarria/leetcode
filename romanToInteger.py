class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        
        for i in range(len(s) - 1):
            total += self.convertCharacter(s[i], s[i+1])
        
        return total + self.convertCharacter(s[-1], "")
        
        
    def convertCharacter(self, cur, after):
        if cur == "M":
            return 1000
        elif cur == "D" and after == "M":
            return -500
        elif cur == "D":
            return 500
        elif cur == "C" and (after == "D" or after == "M"):
            return -100
        elif cur == "C":
            return 100
        elif cur == "L":
            return 50
        elif cur == "X" and (after == "C" or after == "L"):
            return -10
        elif cur == "X":
            return 10
        elif cur == "V":
            return 5
        elif cur == "I" and (after == "X" or after == "V"):
            return -1
        elif cur == "I":
            return 1
        else:
            return 0