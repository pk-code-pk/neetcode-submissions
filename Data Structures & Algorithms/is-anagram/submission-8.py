from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pee = Counter(s)
        poo = Counter(t)
        return pee == poo