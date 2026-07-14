class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = str()

        for i in s:
            if i == " ":
                continue
            if i.isalnum():
                ns += i.lower()

        n = len(ns)
        
        splt = n // 2

        for i in range(n):
            ni = i + 1
            if ns[i] == ns[-ni]:
                continue
            return False

        return True