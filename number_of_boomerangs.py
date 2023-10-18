class Solution:
    def numberOfBoomerangs(self, points):
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n
