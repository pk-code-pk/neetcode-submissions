class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {} 
        for i in range(len(nums) - 1, -1, -1):
            y = target - nums[i]
            if y in mydict:
                return [i, mydict.get(y)]
            mydict[nums[i]] = i