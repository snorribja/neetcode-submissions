class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window size - count of the most frequent character ≤ k
        
        count = {}
        l = 0
        maxf = 0 
        maxlen = 0 

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                  count[s[l]] -= 1
                  l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen