
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {} 
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                hashs[s[i]] = hashs.get(s[i], 0) + 1
                hasht[t[i]] = hasht.get(t[i], 0) + 1 
            for char in s:
                if hashs.get(char,0) != hasht.get(char,0):
                    return False
        return True 