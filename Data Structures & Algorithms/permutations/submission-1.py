class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums,idx):
            if idx == len(nums):
                res.append(nums[::])
                return
            for i in range(idx, len (nums)):
                print(idx)
                print(i)
                print(nums)
                nums[idx], nums[i] = nums[i],nums[idx]
                print(nums)
                
                backtrack(nums,idx+1)
                nums[idx], nums[i] = nums[i],nums[idx]
        res = []
        backtrack(nums,0)
        return res