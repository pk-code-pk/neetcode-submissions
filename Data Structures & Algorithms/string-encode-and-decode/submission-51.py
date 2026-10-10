class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = [] 
        for s in strs:
            ans.append(str(len(s)) + "#" + s)
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans = [] 
        i = 0 
        while i < len(s):
            j = s.index("#",i)
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i = j + length + 1
        return ans 