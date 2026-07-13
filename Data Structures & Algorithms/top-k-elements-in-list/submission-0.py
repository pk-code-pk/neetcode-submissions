class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myhash = {} 
        ans = [] 
        for i in range(len(nums)):
            myhash[nums[i]] = myhash.get(nums[i], 0) + 1 
        x = sorted(myhash, key=myhash.get)
        for i in range(len(x) - 1, len(x) - k - 1, -1):
            ans.append(x[i])
        return ans 
