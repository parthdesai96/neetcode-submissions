class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #s = OUZODYYYXAZV
        #t = XYYZ

        countT = {}
        for x in t:
            countT[x] = 1 + countT.get(x,0)

        window = {}
        resLen = float('infinity')
        res = [-1,-1]
        l = 0
        have,need = 0 , len(countT)

        for r in range(len(s)):
            a = s[r]
            window[a] = 1 + window.get(a,0)

            if a in countT and window[a] == countT[a]:
                have +=1
            
            while have == need:
                if (r - l + 1)< resLen:
                    res = [l,r]
                    resLen = r - l +1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1 
            
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""               
                

