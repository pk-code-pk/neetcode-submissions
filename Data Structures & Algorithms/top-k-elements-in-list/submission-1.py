class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myhash = {} 
        ans = [] 
        for i in range(len(nums)):
            myhash[nums[i]] = myhash.get(nums[i], 0) + 1 
        mylist = [[] for _ in range(len(nums) + 1)]
        for key, value in myhash.items():
            mylist[value].append(key)
        for i in range(len(mylist) - 1, -1, -1):
            if len(ans) >= k:
                break
            for j in range(len(mylist[i])):
                ans.append(mylist[i][j])
        return ans 
