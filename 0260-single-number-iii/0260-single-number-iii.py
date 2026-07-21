class Solution(object):
    def singleNumber(self, nums):
        a={}
        x=[]
        for i in nums:
            a[i]=a.get(i,0)+1
        for key,i in a.items():
            if(i==1):
                x.append(key)
        return x
        