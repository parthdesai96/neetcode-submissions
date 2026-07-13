class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(len(nums)):
                if visited[j] or (j > 0 and nums[j] == nums[j-1] and not visited[j-1]):
                    continue
                visited[j] = True
                cur[i] = nums[j]
                dfs(i+1)
                visited[j] = False

        nums.sort()
        res = []
        cur = [0] * len(nums)
        visited = [False] * len(nums)
        dfs(0)
        return res