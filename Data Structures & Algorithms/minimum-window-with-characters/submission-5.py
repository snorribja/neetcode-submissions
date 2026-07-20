class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        minlen = len(s)
        minstr = "a" * len(s)
        found = False
        t_set = set(t)
        d = {}
        td = {}

        for i in t:
            td[i] = 1 + td.get(i, 0)

        need = len(td)
        count = 0    

        l = 0
        for r in range(len(s)):
            if s[r] in t_set:
                d[s[r]] = 1 + d.get(s[r], 0)
                if d[s[r]] == td[s[r]]:
                    count += 1

            while l < r and (s[l] not in t_set or d[s[l]] > td[s[l]] or (r - l + 1) > minlen): 
                if s[l] in t_set:
                    d[s[l]] -= 1
                    if d[s[l]] < td[s[l]]:
                        count -= 1
                l += 1

            if count == need: 
                checklen = len(s[l:r+1])
                if found and checklen < minlen:
                    minstr = s[l:r+1]
                    minlen = checklen
                elif checklen <= minlen: 
                    found = True
                    minstr = s[l:r+1]
                    minlen = checklen
        
        if found:
            return minstr
        return ""