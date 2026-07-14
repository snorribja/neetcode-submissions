class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        r = ""
        for w in strs:
            if not w:
                r = r + ", "
                continue
            for j in w:
                r = r + f"{str(ord(j))},"
            r = r[:-1] + " "
        return r[:-1]
            
    def decode(self, s: str) -> List[str]:
        if s == "":
            return list()
        r = list()
        sl = s.split(" ")
        for w in sl:
            wl = w.split(",")
            n = ""
            for i in wl:
                if not i:
                    continue        
                n = n + chr(int(i))
            r.append(n)
        return r
