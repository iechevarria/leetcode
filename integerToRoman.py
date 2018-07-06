class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        ret = ""
                
        num = list(str(num).zfill(4))
        num = [int(x) for x in num]
        
        cur = num.pop()
        if cur < 4:
            ret = "I" * cur
        elif cur == 4:
            ret = "IV" 
        elif cur < 9:
            ret = "V" + (cur - 5) * "I"      
        elif cur == 9:
            ret = "IX"
        
        cur = num.pop()
        if cur < 4:
            ret = "X" * cur + ret
        elif cur == 4:
            ret = "XL" + ret
        elif cur < 9:
            ret = "L" + (cur - 5) * "X" + ret
        elif cur == 9:
            ret = "XC" + ret
            
        cur = num.pop()
        if cur < 4:
            ret = "C" * cur + ret
        elif cur == 4:
            ret = "CD" + ret
        elif cur < 9:
            ret = "D" + "C" * (cur - 5) + ret
        elif cur == 9:
            ret = "CM" + ret
        
        return "M" * num.pop() + ret
