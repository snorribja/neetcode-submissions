class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        r = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return list(i[0] for i in r[:k])