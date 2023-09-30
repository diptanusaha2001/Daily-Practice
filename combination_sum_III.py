class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.comb([], 1, k, n)
        return self.ans
    def comb(self, ds,start, k, target):
        if k == 0 and target == 0:
            self.ans.append(ds)
            return 
        if k == 0 or target <= 0:
            return 
        for i in range(start,10):
            self.comb(ds + [i], i + 1, k - 1, target - i)
