class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int Sum = 0;
        for (int i=0;i<k;i++){
            Sum += nums[i];
        }
        int Max = Sum;
        for (int i=k;i<n;i++){
            Sum = Sum-nums[i-k]+nums[i];
            if (Sum > Max){
                Max = Sum;
            }
        }
        return (double)Max / k;
    }
};;