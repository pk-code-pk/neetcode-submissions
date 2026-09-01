class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {} 
        hasht = {}
        for letter in s:
            hashs[letter] = hashs.get(letter,0) + 1
        for letter in t:
            hasht[letter] = hasht.get(letter,0) + 1
        if hashs == hasht:
            return True
        return False 
            