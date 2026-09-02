class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] = seen.get(nums[i], 0) + 1 
            else:
                seen[nums[i]] = 1
            
        newlist = sorted(seen.items(), key = lambda kv: kv[1])
        newerlist = [kv[0] for kv in newlist]
        return newerlist[len(newerlist) - k: len(newerlist)]
