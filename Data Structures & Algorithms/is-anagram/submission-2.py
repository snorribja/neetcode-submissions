class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        d2 = dict()
        
        for i in s:
            if i not in d:
                d[i] = 1
            else: 
                d[i] += 1

        for i in t:
            if i not in d2:
                d2[i] = 1
            else: 
                d2[i] += 1
            
        return d == d2 