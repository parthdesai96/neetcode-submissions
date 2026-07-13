class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        minlength = float('inf')
        for r in range(len(nums)):
            currSum+=nums[r]
           
            while currSum>=target:
                minlength = min(minlength,r-l+1)
                print(minlength)
                currSum -= nums[l]
                l+=1

        return minlength if minlength!= float('inf') else 0
            
