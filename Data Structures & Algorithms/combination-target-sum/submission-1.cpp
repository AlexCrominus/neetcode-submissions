class Solution {
public:
    vector<vector<int>> ret;

    void bfs(vector<int>& nums, int target, int idx, vector<int>& sublists) {
        if (target == 0) {
            ret.push_back(sublists);
            return;
        }
        
        if (idx == nums.size() || target < 0) {
            return;
        }

        sublists.push_back(nums[idx]);
        target -= nums[idx];
        bfs(nums, target, idx, sublists);
        target += nums[idx];
        sublists.pop_back();

        bfs(nums, target, idx+1, sublists);
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> sublists;
        bfs(nums, target, 0, sublists);

        return ret;
    }
};
