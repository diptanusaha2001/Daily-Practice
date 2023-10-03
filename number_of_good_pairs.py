class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] map = new int[101];
        int res = 0;
        for (int num : nums) {
            res += map[num]++;
        }
        return res;
    }
}
