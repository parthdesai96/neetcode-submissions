class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        resMap =defaultdict(int)
        bucketList = [[] for a in range(len(nums)+1)]

        for i in nums:
            resMap[i] +=1
        
        for num, index in resMap.items():
            bucketList[index].append(num)
        
        result = []
        for bucket in range(len(bucketList) -1 ,0, -1):
            for i in bucketList[bucket]:
                result.append(i)
                if(k == len(result)):
                    return result
        