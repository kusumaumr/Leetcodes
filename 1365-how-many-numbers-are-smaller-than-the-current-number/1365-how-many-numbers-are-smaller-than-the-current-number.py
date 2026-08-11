class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]

        for val in nums:
            c=0
            for val1 in nums:
                if val1<val:
                    c+=1
            l.append(c)
        return l