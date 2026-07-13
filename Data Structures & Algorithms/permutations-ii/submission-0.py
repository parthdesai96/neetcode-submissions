class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[::])
                return
            for i in range(idx, len (nums)):
                if i > idx and nums[i] == nums[idx]:
                    continue
                nums[idx], nums[i] = nums[i],nums[idx]
                backtrack(idx+1)
            for i in range(len(nums)-1, idx, -1):
                nums[idx], nums[i] = nums[i],nums[idx]
        res = []
        nums.sort()
        backtrack(0)
        return res