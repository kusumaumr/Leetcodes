class Solution(object):
    def missingNumber(self, nums):
        a=0
        b=0
        for i in range(len(nums)+1):
            a^=i
        for j in nums:
            b^=j

        
        return a^b
        