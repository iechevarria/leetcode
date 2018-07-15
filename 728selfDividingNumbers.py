class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(left, right + 1):
            nums = [int(x) for x in list(str(i))]
            
            if 0 not in nums:
                ok = True
                for num in nums:
                    if i % num != 0:
                        ok = False
                
                if ok: res.append(i)
        
        return res