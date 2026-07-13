
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myhash = {} 
        if len(s) != len(t): 
            return False 
        for i in range(len(s)):
            myhash[s[i]] = myhash.get(s[i],0) + 1 
            myhash[t[i]] = myhash.get(t[i], 0) - 1 
        for i in range(len(s)):
            if myhash.get(s[i]) != 0:
                return False 
        return True 
