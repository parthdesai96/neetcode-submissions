class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                dfs(j+1,total+nums[j])
                cur.pop()
        

        nums.sort()
        res = []
        cur = []
        dfs(0,0)
        return res