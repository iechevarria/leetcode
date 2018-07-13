class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if k == 0:
            return
        
        shift = k % len(nums)
        tmp = [0] * len(nums)
        
        for i in range(len(nums)):
            tmp[i] = nums[(i - shift) % len(nums)]

        for i in range(len(nums)):
            nums[i] = tmp[i]
            