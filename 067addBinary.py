class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        total = ''
        
        a = list(a)
        b = list(b)
        
        carry = 0
        
        while a or b:
            if a and b:
                tmp = int(a.pop()) + int(b.pop()) + carry
            elif a:
                tmp = int(a.pop()) + carry
            elif b:
                tmp = int(b.pop()) + carry
            total = '1' + total if tmp % 2 == 1 else '0' + total
            carry = 1 if tmp > 1 else 0
                
        total = '1' + total if carry > 0 else total
        return total if len(total) > 0 else '0'
