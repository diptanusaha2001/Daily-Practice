class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.soln1(p1, p2, p3, p4)
    
    def soln1(self, p1, p2, p3, p4):
        count = collections.Counter()
        coordinates = [p1, p2, p3, p4]
        
        for i, (xi, yi) in enumerate(coordinates):
            for xj, yj in coordinates[i+1:]:
                d = (xi-xj)**2 + (yi-yj)**2
                count[d] += 1
                if d==0 or len(count) > 2: return False
                
        return len(count)==2 and all(count[i] in {2, 4} for i in count)
