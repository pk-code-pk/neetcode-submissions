class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + "*" + str(len(s)) + "_" + s
        return encoded 

    def decode(self, s: str) -> List[str]:
        mylist = [] 
        for i in range(len(s)):
            if s[i] == "_" and s[i-1].isnumeric():
                length = ""
                j = i-1
                while s[j].isnumeric():
                    length = s[j] + length 
                    j = j - 1
                mylist.append(s[i+1:i+int(length)+1])
        return mylist


