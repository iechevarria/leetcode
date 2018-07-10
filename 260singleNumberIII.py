class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        singles = []
        
        for i in range(len(nums)):
            cur = nums.pop()
            if cur in singles:
                singles.remove(cur)
            else:
                singles.append(cur)
            
        return singles