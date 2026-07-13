class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"}":"{",")":"(","]":"["}

        for x in s: 
            if x in openToClose:
                if stack and stack[-1] == openToClose[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False