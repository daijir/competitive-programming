#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = le9;

struct SegmentTree {
    int n;
    vector<int> min_tree, max_tree;

    SegmentTree(int size) {
        n = 1;
        while (n < size) n *= 2;
        min_tree.assign(2 * n, INF);
        max_tree.assign(2 * n, -INF);
    }

    void update(int idx, int val) {
        int i = idx + n - 1;
        min_tree[i] = val;
        max_tree[i] = val;
        while (i > 1) {
            i /= 2;
            min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1]);
            max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1]);
        }
    }
}