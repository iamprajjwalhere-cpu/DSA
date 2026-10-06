class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> check;
        int n = nums.size();
        for (int i = 0;i<n;i++){
            if (check.count(nums[i])){
                return true;
            }
            check.insert(nums[i]);
            if (check.size() > k) {
                check.erase(nums[i - k]);
            }
        }
        return false;
    }
};