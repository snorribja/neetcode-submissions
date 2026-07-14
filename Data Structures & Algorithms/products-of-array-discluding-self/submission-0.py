import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [1] * len(nums)
        for i,j in enumerate(nums):
            st = x[i]
            x = [v * j for v in x]
            x[i] = st
        return x