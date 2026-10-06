class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [] 
        for s in strs:
            encoded.append(str(len(s))+"#"+s)
        return "".join(encoded)
            
    def decode(self, s: str) -> List[str]:
        i = 0 
        ans = [] 
        while i < len(s):
            j = s.index("#",i)
            length = s[i:j]
            ans.append(s[j+1:j+1+int(length)])
            i = j+1+int(length)
        return ans 
