class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
                
        row = [1]
        
        for i in range(rowIndex + 1):
            new = [1] * (i + 1)
            for j in range(1, i):
                new[j] = row[j-1] + row[j]
            row = new
    
        return row