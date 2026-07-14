class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        maxlen = 0
        s_set = set()
        for r in range(len(s)):
            let = s[r]
            while let in s_set and l < r:
                s_set.remove(s[l])
                l += 1
            s_set.add(let)
            maxlen = max(maxlen, len(s_set))

        return maxlen