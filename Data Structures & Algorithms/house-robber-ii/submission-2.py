class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(0, nums[1:], {}), self.helper(0, nums[:-1], {}))

    
    def helper(self, i, nums, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0


        memo[i] = max(nums[i] + self.helper(i+2, nums, memo), self.helper(i+1, nums, memo))

        return memo[i]
