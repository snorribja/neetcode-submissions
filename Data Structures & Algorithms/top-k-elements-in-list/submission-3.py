class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tdict = dict()
        for i in nums:
            if i in tdict:
                tdict[i] += 1
            else:
                tdict[i] = 1
        titems = list(tdict.items())
        ret_lst = list()
        while k != 0:
            mmax = 0
            r = None
            stor = None
            for i in range(len(titems)):
                if mmax < titems[i][1]:
                    mmax = titems[i][1]
                    r = titems[i][0]
                    stor = i
            ret_lst.append(r)
            del titems[stor]
            k = k - 1
        return ret_lst