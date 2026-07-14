class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, i in enumerate(nums):
            for ind2, j in enumerate(nums):
                if ind == ind2:
                    continue
                elif j+i == target:
                    return [ind, ind2]