class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret_list = list()

        for l in range(len(nums)-k+1):
            ret_list.append(max(nums[l:l+k]))
        
        return ret_list