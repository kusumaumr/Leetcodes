class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]

        for i in nums:
            c=0
            for k in nums:
                if k<i:
                    c+=1
            l.append(c)
        return l