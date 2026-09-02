class Solution:

    def encode(self, strs: List[str]) -> str:
        bigword = [] 
        for word in strs:
            bigword.append(str(len(word)) + "#" + word + "!")
        return "".join(bigword)








    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i - 1
            if s[i] == "#" and s[j].isnumeric():
                length = []
                while s[j].isnumeric():
                    length.append(s[j])
                    j = j - 1
                length.reverse()
                x = int("".join(length))
                final.append(s[i+1:i+x+1])
                i = i + 1 + x
            else:
                i = i + 1
        return final 

            
                    


