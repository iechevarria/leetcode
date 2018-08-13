class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = list(set(nums))
        if len(setNums) < 1:
            return
        elif len(setNums) < 3:
            return max(setNums)
        else:
            setNums.remove(max(setNums))
            setNums.remove(max(setNums))
            return max(setNums)
        