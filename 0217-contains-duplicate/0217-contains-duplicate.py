class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_found=False
        d={}   
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for k,v in d.items():
            if v>1:
                is_found=True
                break
        return is_found
