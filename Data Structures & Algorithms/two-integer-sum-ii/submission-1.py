class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums) - 1

        while l < r:
            cursum = nums[l] + nums[r]
            if cursum > target:
                r -=1
            elif cursum< target:
                l +=1
            elif cursum == target:
                return [l+1,r+1]

        return []