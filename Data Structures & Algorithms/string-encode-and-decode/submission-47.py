class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = [] 
        for word in strs:
            ans.append(str(len(word)) + "#" + word)
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans = [] 
        i = 0 
        while i < len(s):
            j = s.index("#",i)
            length = s[i:j]
            ans.append(s[j+1:j+1+int(length)])
            i=j+1+int(length)
        return ans 