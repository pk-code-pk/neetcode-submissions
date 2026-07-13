class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {} 
        for i in range(len(strs)):
            mydict["".join(sorted(strs[i]))] = mydict.get("".join(sorted(strs[i])), [])
            mydict["".join(sorted(strs[i]))].append(strs[i])
        return list(mydict.values())