class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mset = set()
        for i in nums:
            if i in mset:
                return True
            else:
                mset.add(i)
        return False
