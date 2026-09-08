class Solution:

    def encode(self, strs: List[str]) -> str:
        final = [] 
        for word in strs:
            final += str(len(word)) + "#" + word 
        return "".join(final)
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            j = int(s.index("#",i))
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+length+1
        return ans 