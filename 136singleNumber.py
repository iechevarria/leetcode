class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        single = []
        
        for i in range(len(nums)):
            cur = nums.pop()
            if cur in single: 
                single.remove(cur)
            else:
                single.append(cur)
        
        return single[0]