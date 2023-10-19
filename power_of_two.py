class Solution {
public:
    bool isPowerOfTwo(int n) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        
        if(n == 0) return false;
        if(n == 1) return true;

        while((n % 2) == 0)
        {
            n = n / 2;
        }

        return n == 1;
    }
};
