from bisect import bisect

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {num: i for i, num in enumerate(nums2)}
        n = len(nums1)
        idx_f, idx_b = [0], [0]
        front, back = [dic[nums1[0]]], [dic[nums1[-1]]]
        for num in nums1[1:]:
            idx = bisect(front, dic[num])
            front.insert(idx, dic[num])
            idx_f.append(idx)
        
        for num in nums1[n-2::-1]:
            
            idx = bisect(back, dic[num])
            idx_b.append(len(back) - idx)
            back.insert(idx, dic[num])
                
            
        idx_b = idx_b[::-1]
        
        return sum(a*b for a, b in zip(idx_f, idx_b))
