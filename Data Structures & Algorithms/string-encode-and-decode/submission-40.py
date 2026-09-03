class Solution:

    def encode(self, strs: List[str]) -> str:
        newword = []
        for word in strs:
            newword.append(str(len(word)) + "#" + word)
        return "".join(newword)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            j = s.index("#", i)
            length = s[i:j] 
            ans.append(s[j+1:j+1+int(length)])
            i = j+1+int(length)
        return ans 
