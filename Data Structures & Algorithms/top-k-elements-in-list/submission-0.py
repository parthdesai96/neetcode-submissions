class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        lister = [[] for i in range(len(nums)+1)]

        for i in nums:
            numMap[i] += 1
        for num,cnt in numMap.items():
            lister[cnt].append(num)

        res = []
        for i in range(len(lister) - 1,0, -1):
            for num in lister[i]:
                res.append(num)
                if len(res) == k:
                    return res
