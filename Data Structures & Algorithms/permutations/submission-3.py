class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(len(nums)):
                if not visited[j]:
                    visited[j] = True
                    cur[i] = nums[j]
                    dfs(i+1)
                    visited[j] = False

        res = []
        cur = [0] * len(nums)
        visited = [False] * len(nums)
        dfs(0)
        return res
        