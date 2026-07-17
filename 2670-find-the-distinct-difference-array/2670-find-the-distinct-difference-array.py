class Solution(object):
    def distinctDifferenceArray(self, nums):
        res=[]
        
        for i in range(len(nums)):
            left=len(set(nums[ :i+1]))
            right=len(set(nums[i+1:]))
            res.append(left-right)
        return res

        
        