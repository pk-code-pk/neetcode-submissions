class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsnew = nums.copy() 
        total = 1 
        totaltwo = 1 
        i = 0 
        j = len(nums) - 1 
        while i < len(nums):
            save = nums[i]
            numsnew[i] = total 
            total *= save
            i += 1 
        while j > -1:
            savetwo = nums[j] 
            numsnew[j] *= totaltwo
            totaltwo *= savetwo  
            j -=1 
        return numsnew 


            

