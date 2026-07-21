class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {'(':')','{':'}','[':']', ')':'a','}':'a',']':'a'}
        n = len(s)
        if n % 2 == 1: 
            return False
        # valid_dict[s[i]]
        stack = list()

        for c in s:
            if len(stack) == 0 or valid_dict[stack[-1]] != c:
                stack.append(c)
                continue
            
            stack.pop()

        if len(stack) == 0:
            return True
        return False
        
        c not in valid_dict