class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        single = []
        double = []
        
        for i in range(len(nums)):
            
            cur = nums.pop()
            
            if cur in double:
                single.remove(cur)
                double.remove(cur)
            elif cur in single:
                double.append(cur)
            else: 
                single.append(cur)
            
        return single[0]
            
            