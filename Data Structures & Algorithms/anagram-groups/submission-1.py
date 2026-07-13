class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {} 
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            mydict.setdefault(key, []).append(strs[i])
        return list(mydict.values())