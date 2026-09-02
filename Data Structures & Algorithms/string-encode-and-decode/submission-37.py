class Solution:

    def encode(self, strs: List[str]) -> str:
        bigword = [] 
        for word in strs:
            bigword.append(str(len(word)) + "#" + word)
        return "".join(bigword)








    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            final.append(s[j+1:j+1+length])
            i = j+1+length
        return final
            
                    


