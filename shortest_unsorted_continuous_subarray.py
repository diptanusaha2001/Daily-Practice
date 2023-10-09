class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxi = INT_MIN, mini = INT_MAX;
        int index1 = 0, index2 = 0;
        
        if(n == 1) return 0;
        for(int i = 0; i < n; i++)
        {
            if(i == 0)
            {
                if(nums[i] > nums[i+1])
                {
                    maxi = max(maxi, nums[i]);
                    mini = min(mini, nums[i]);
                }
            }
            else if(i == n - 1)
            {
                if(nums[i] < nums[i - 1])
                {
                    maxi = max(maxi, nums[i]);
                    mini = min(mini, nums[i]);
                }
            }
            else 
            {
                if(nums[i] > nums[i+1] || nums[i] < nums[i-1])
                {
                    maxi = max(maxi, nums[i]);
                    mini = min(mini, nums[i]);
                }
            }
        }
        for(int i = 0; i < n; i++)
        {
            if(nums[i] > mini)
            {
                index1 = i;
                break;
            }
        }
        for(int i = 0; i < n; i++)
        {
            if(nums[i] < maxi)
            {
                index2 = i;
            }
        }
        if(maxi == INT_MIN) return 0;
        else return index2 - index1 + 1;
    }
};
