class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return
        
        l = 0
        r = 0
        
        while r < len(nums) and l < len(nums):
            if nums[r] == 0 or r == l:
                r += 1
            elif nums[l] != 0:
                l += 1
            elif nums[l] == 0 and nums[r] != 0:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
        