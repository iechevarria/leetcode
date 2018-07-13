class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del(nums[i])
            else:
                i += 1
             
        return len(nums)

    
    def removeElementAlt(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        length = len(nums)
        
        while l <= r: 
            if nums[l] == val:
                nums[l] = nums[r]
                length -= 1
                r -= 1
            else:
                l += 1
        
        return length