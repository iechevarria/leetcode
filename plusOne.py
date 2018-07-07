class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits[-1] += 1
                
        for i in range(len(digits)):
            if digits[-i] > 9 and len(digits) > 1:
                digits[-i-1] += 1
                digits[-i] -= 10

        if digits[0] > 9:
            digits[0] -= 10
            digits = [1] + digits
        
        return digits