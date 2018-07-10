class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ct = 0
        
        for s in S:
            if s in J:
                ct += 1
        
        return ct