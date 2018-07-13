class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        triangle = []
        
        for i in range(numRows):
            cur = [1] * (i + 1)  
            if i > 0:
                for j in range(1, len(cur)-1):
                    cur[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(cur)
                        
        return triangle
    