class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)
        compl = 0 

        for i,n in enumerate(nums):
            compl = target - n
            print(numMap)
            if compl in numMap:
                return [numMap[compl],i]
            numMap[n] = i

        return []