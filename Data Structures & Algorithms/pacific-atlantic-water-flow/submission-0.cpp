class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> ret(
            heights.size(),
            vector<int>(heights[0].size(), 0)
        );

        for (int i = 0; i < heights.size(); i++) {
            for (int j = 0; j < heights[0].size(); j++) {

                vector<vector<bool>> visit(
                    heights.size(),
                    vector<bool>(heights[0].size(), false)
                );

                dfs(i, j, heights, ret, visit);
            }
        }

        // Convert your 0/1 matrix into the format LeetCode wants
        vector<vector<int>> ans;

        for (int i = 0; i < heights.size(); i++) {
            for (int j = 0; j < heights[0].size(); j++) {
                if (ret[i][j]) {
                    ans.push_back({i, j});
                }
            }
        }

        return ans;
    }

    pair<int, int> dfs(
        int r,
        int c,
        vector<vector<int>>& heights,
        vector<vector<int>>& ret,
        vector<vector<bool>>& visit
    ) {
        // Pacific
        if (r < 0 || c < 0) {
            return {true, false};
        }

        // Atlantic
        if (r >= heights.size() || c >= heights[0].size()) {
            return {false, true};
        }

        visit[r][c] = true;

        pair<int, int> flow = {false, false};

        // DOWN
        if (
            r + 1 >= heights.size()
        ) {
            flow.second = true;
        }
        else if (
            !visit[r + 1][c] &&
            heights[r][c] >= heights[r + 1][c]
        ) {
            auto [p1, a1] = dfs(
                r + 1, c, heights, ret, visit
            );

            flow.first |= p1;
            flow.second |= a1;
        }

        // UP
        if (r - 1 < 0) {
            flow.first = true;
        }
        else if (
            !visit[r - 1][c] &&
            heights[r][c] >= heights[r - 1][c]
        ) {
            auto [p2, a2] = dfs(
                r - 1, c, heights, ret, visit
            );

            flow.first |= p2;
            flow.second |= a2;
        }

        // RIGHT
        if (c + 1 >= heights[0].size()) {
            flow.second = true;
        }
        else if (
            !visit[r][c + 1] &&
            heights[r][c] >= heights[r][c + 1]
        ) {
            auto [p3, a3] = dfs(
                r, c + 1, heights, ret, visit
            );

            flow.first |= p3;
            flow.second |= a3;
        }

        // LEFT
        if (c - 1 < 0) {
            flow.first = true;
        }
        else if (
            !visit[r][c - 1] &&
            heights[r][c] >= heights[r][c - 1]
        ) {
            auto [p4, a4] = dfs(
                r, c - 1, heights, ret, visit
            );

            flow.first |= p4;
            flow.second |= a4;
        }

        if (flow.first && flow.second) {
            ret[r][c] = 1;
        }

        return flow;
    }
};