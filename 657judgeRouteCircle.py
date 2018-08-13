class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        x = 0
        y = 0
        
        moves = list(moves)
        
        for move in moves:
            if move == "L":
                x -= 1
            elif move == "R":
                x += 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
        
        return True if x == 0 and y == 0 else False