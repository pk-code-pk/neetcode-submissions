class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = [] 
        for index, num in enumerate(nums): 
            mydict[num].append(index)
        i = len(nums) - 1 
        while i > -1:
            y = target - nums[i]
            if y in mydict and nums[i] != y: 
                return [mydict.get(y)[0],mydict.get(nums[i])[0]]
            if y in mydict and nums[i] == y: 
                return [mydict.get(y)[0],mydict.get(y)[1]]
            i = i - 1 
        
        
