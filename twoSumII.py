class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        j = len(numbers) - 1
        
        while True:
            nsum = numbers[i] + numbers[j]
            if nsum == target:
                return [i+1, j+1]
            elif nsum > target:
                j -= 1
            elif nsum < target:
                i += 1
