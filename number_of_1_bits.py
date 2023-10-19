class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        ans = 0
        for c in s:
            if c == '1':
                ans += 1
        return ans
