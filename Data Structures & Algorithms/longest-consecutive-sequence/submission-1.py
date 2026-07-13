class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = 0
        store = set(nums)

        for i in store:
            if (i-1) not in store:
                length = 1
                while(i+length) in store:
                    length+=1
                count = max(length,count)
        return count
            
        return count