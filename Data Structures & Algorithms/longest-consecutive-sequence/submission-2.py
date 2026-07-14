class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        ns = set(nums)
        nd = dict()
        
        for i in ns:
            nd[i] = False

        starter_ints = list()

        seen_counter = 0
        while not all(nd.values()):
            if nd[nums[seen_counter]]:
                seen_counter += 1
                continue
            nd[nums[seen_counter]] = True

            lower_num = nums[seen_counter] - 1
            if lower_num in ns:
                seen_counter += 1
                continue
            
            starter_ints.append(nums[seen_counter])
            seen_counter += 1

        best_c = 1
        for i in starter_ints:
            curr_c = 1
            n = i + 1
            while n in ns:
                curr_c += 1
                n += 1
            if curr_c > best_c:
                best_c = curr_c 

        return best_c

