class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) < 1:
            return []
        
        height = len(matrix)
        width = len(matrix[0])
        
        new = []
        
        x = 0
        y = 0
        up = True
        
        for i in range(width * height):
            new.append(matrix[y][x])
            if x == width - 1 and up:
                y += 1
                up = False
            elif y == height - 1 and not up:
                x += 1
                up = True
            elif y == 0 and up:
                x += 1
                up = False
            elif x == 0 and not up:
                y += 1
                up = True
            elif up: 
                x += 1
                y -= 1
            elif not up:
                x -= 1
                y += 1
                
        return new
