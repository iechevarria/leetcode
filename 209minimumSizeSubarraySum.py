class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 1 or s == 0:
            return 0
        
        l = 0
        r = 0
        curSum = nums[l]
        final = None
        
        while r < len(nums):
            try:
                if curSum < s:
                    r += 1
                    curSum += nums[r]
                    if final:  
                        curSum -= nums[l]
                        l += 1
                else:
                    final = curSum
                    curSum -= nums[l]
                    l += 1
            except IndexError:
                return r - l + 1 if final else 0
            
        return r - l + 1 if final else 0
        