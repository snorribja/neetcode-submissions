class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        return self.helper(0, nums, memo)

    
    def helper(self, i, nums, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0

        memo[i] = max(nums[i] + self.helper(i+2, nums, memo), self.helper(i+1, nums, memo))

        return memo[i]