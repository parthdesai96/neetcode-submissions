class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i,n in enumerate(nums):
            compl = target - nums[i]
            if compl in numMap:
                return [numMap[compl],i]
            numMap[n] = i
        return []