class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = max(nums)
        l=[]
        for i in range(x):
            if i not in nums:
                return i
                break
        else:
            return x+1
