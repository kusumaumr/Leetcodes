class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_found=False
        nums.sort()   
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                is_found=True
                break
        return is_found
