class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        front = 0
        while front < len(nums) -1 and nums[front] <= nums[front+1]:
            front +=1
        
        if front == len(nums)-1:
            return 0
        
        back = len(nums) -1
        while nums[back] >= nums[back-1]:
            back -=1
        
        max_ = max(nums[front:back+1])
        min_ = min(nums[front:back+1])

        while front >0 and nums[front-1] > min_:
            front -=1
        
        while back < len(nums)-1 and nums[back+1] < max_:
            back +=1
        
        return back - front + 1
