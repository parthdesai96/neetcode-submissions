class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        for i in range(len(nums),-1,-1):
            if i == k:
                return heapq.heappop(nums)
            heapq.heappop(nums)

        