class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            def dfs(openC,closeC,path):
                if openC> n or closeC>n or openC<closeC:
                    return
                if openC == n and closeC==n:
                    combinations.append(path)
                    return
                
                dfs(openC+1,closeC,path+'(')
                dfs(openC,closeC+1,path+')')


            combinations =[]
            dfs(0,0,'')
            return combinations
