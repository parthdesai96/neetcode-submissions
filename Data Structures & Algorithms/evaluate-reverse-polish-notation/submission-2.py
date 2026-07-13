class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif s == "-":
                a,b = stack.pop() , stack.pop()
                stack.append(b-a)
            elif s == "*":
                mult = (stack.pop() * stack.pop())
                stack.append(mult)
            elif s == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(s))
        return stack.pop()
            
            