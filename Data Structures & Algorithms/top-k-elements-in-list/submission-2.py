class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        result = [[]for i in range(len(nums)+1)]

        for i in nums:
            numMap[i] += 1

        for num, count in numMap.items():
            result[count].append(num)

        res = []
        for i in range(len(result) -1 , 0 , -1):
            for num in result[i]:
                res.append(num)
                if len(res) == k: 
                    return res
