class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls2 = len(s2)
        ls1 = len(s1)

        if ls1 > ls2:
            return False
        d1 = {}
        for c in s1:
            d1[c] = 1 + d1.get(c, 0)

        need = len(d1)
        
        d2 = {}
        count = 0 
        l = 0

        for r in range(ls2):
            if s2[r] in d1:
                d2[s2[r]] = 1 + d2.get(s2[r], 0)
                if d2[s2[r]] == d1[s2[r]]:
                    count += 1

            while (r - l + 1) > ls1:
                if s2[l] in d1:
                    if d2[s2[l]] == d1[s2[l]]:
                        count -= 1
                    d2[s2[l]] -= 1
                l += 1
                
            if need == count:
                return True

        return False


