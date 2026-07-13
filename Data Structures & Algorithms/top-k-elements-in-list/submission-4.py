class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        buckets = [[] for a in range(len(nums)+1)]

        for x in nums:
            numMap[x] += 1
        
        for num,index in numMap.items():
            buckets[index].append(num)

        result = []
        for b in range(len(buckets) -1, 0, -1):
            for i in buckets[b]:
                result.append(i)
                if(k == len(result)):
                    return result