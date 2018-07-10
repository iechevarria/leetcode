class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        elements = {}
        
        for i in range(len(nums)):
            if str(nums[i]) not in elements:
                elements[str(nums[i])] = 1
            else:
                elements[str(nums[i])] += 1
        
        for key in elements:
            if elements[key] > math.floor(len(nums)/2):
                return int(key)
            
        