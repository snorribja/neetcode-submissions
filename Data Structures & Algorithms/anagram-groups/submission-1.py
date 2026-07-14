class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            k = dict()
            for i in s:
                if i in k:
                    k[i] += 1
                else:
                    k[i] = 1
            kh = tuple(sorted(k.items()))
            if kh in d:
                d[kh].append(s)
            else:
                d[kh] = [s]
        return list(d.values())