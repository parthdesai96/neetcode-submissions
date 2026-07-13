class Solution:
    def checkValidString(self, s: str) -> bool:
         maxleft, minleft = 0,0

         for c in s:
            if c == "(":
                maxleft,minleft = maxleft+1,minleft+1
            elif c == ")":
                maxleft,minleft = maxleft-1,minleft-1
            else:
                maxleft,minleft = maxleft+1,minleft-1
            
            if maxleft<0:
                return  False

            if minleft<0:
                minleft = 0

         return minleft == 0
