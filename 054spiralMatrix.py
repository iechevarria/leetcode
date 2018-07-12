class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        try:
            width = len(matrix[0])
        except IndexError:
            return []
        
        height = len(matrix)
        
        new = []
                
        x = 0
        y = 0
        
        d = 'r'
        
        lbound = 0
        rbound = width - 1
        tbound = 0
        bbound = height - 1
        
        for i in range(height * width):
            new.append(matrix[y][x])
            if d == 'r':
                if x < rbound:
                    x += 1
                else:
                    d ='d'
                    tbound += 1
                    y += 1        
            elif d == 'l':
                if x > lbound:
                    x -= 1
                else:
                    d = 'u'
                    bbound -= 1
                    y -= 1
            elif d == 'u':
                if y > tbound:
                    y -= 1
                else:
                    d = 'r'
                    lbound += 1
                    x += 1
            elif d == 'd':
                if y < bbound:
                    y += 1
                else:
                    d = 'l'
                    rbound -= 1
                    x -= 1
                    
        return new
