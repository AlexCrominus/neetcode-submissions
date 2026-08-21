class Solution {
public:
    vector<vector<int>> ret;
    void bfs(vector<int>& nums, vector<int>& sublist, int idx) {
        if (idx == nums.size()) {
            ret.push_back(sublist);
            return;
        }

        sublist.push_back(nums[idx]);

        bfs(nums, sublist, idx+1);
        sublist.pop_back();
        bfs(nums, sublist, idx+1);
    } 
    
    vector<vector<int>> subsets(vector<int>& nums) {

        vector<int> sublist;
        bfs(nums, sublist, 0);

        return ret;
    }
};
