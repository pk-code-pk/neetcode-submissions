class Solution:

    def encode(self, strs: List[str]) -> str:
        new = [] 
        for word in strs:
            new.append(str(len(word)) + "#" + word)
        return "".join(new)
    def decode(self, s: str) -> List[str]:
        i = 0 
        ans = [] 
        while i < len(s):
            index = s.index("#",i)
            length = int(s[i:index])
            word = s[index + 1 : index + 1 + length]
            ans.append(word)
            i = index+1+length
        return ans 

