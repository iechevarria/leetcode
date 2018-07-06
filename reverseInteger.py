class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        flipped = str(x)[::-1]
        flipped = int(flipped) if "-" not in flipped else int("-" + flipped[:-1])
                
        return flipped if (flipped < 2**31 - 1 and flipped > -2**31) else 0
