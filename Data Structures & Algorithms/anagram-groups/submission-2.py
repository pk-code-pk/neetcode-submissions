
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} 
        ans = [] 
        for word in strs:
            key = "".join(sorted(word))
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        
        
        listofkeys = list(seen.keys())
    
        for key in listofkeys:
            ans.append(seen[key])
        return ans 
            
                

