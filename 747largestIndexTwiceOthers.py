class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxElement = max(nums)
        maxIndex = nums.index(maxElement)
        del(nums[maxIndex])
        maxElement /= 2
        
        for num in nums:
            if maxElement < num:
                return -1
        
        return maxIndex
        
        