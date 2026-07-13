class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L , R = 1,max(piles)     
        res = R 

        while L <= R:
            k = (L+R)//2

            Tsum = 0
            for p in piles:
                Tsum += math.ceil(float(p)/k)
            if Tsum <= h:
                res = k
                R = k -1
            else:
                L = k+1
        return res