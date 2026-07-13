class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start_index, total):
            if total == target:
                combinations.append(combination.copy())
                return

            if total > target or start_index >= len(candidates):
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                dfs(i+1,total + candidates[i])
                combination.pop()


        combinations = []
        combination = []
        candidates.sort()
        dfs(0,0)
        return combinations