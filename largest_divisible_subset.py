class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*n
        hsh = [i for i in range(n)]
        max_i, max_v = 0, 1
        
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
                    hsh[i] = j
                    max_i = i if max_v<dp[i] else max_i
                    max_v = max(max_v, dp[i])
        
        seq = []
        while True:
            seq.append(nums[max_i])
            if max_i == hsh[max_i]:
                break
            max_i = hsh[max_i]
        return seq[::-1]
