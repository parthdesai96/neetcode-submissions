class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        windows = {}
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        have, need = 0, len(countT)
        res, reslen = [-1,-1] , float("infinity")
        l = 0
        for r in range (len(s)):
            x = s[r]
            windows[x] = 1 + windows.get(x,0)

            if x in countT and countT[x] == windows[x]:
                have +=1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                
                windows[s[l]] -=1
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    have -=1
                l +=1
        l,r = res
        return s[l:r +1] if reslen != float("infinity") else ""
