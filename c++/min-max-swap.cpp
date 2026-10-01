// https://atcoder.jp/contests/abc476/tasks/abc476_e

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

// strctとclassの違い
// 値型か参照型か
// 値型 - 値のコピー
// 参照型 - アドレスのコピー
// 参照型はコストが高いので、基本的には値型を使う
// struct - 参照型 - 値が変更される
// class - 値型 - 値が変更されない

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

    int query_min(int l, int r, int k = 1, int node_l = 1, int node_r = -1) {
        if (node_r == -1) node_r = n;
        if (r < node_l || node_r < l) return INF;
        if (l <= node_l && node_r <= r) return min_tree[k];
        int mid = (node_l + node_r) / 2;
        return min(query_min(l, r, 2 * k, node_l, mid),
                   query_min(l, r, 2 * k + 1, mid + 1, node_r));
    }

    int query_max(int l, int r, int k = 1, int node_l = 1, int node_r = -1) {
        if (node_r == -1) node_r = n;
        if (r < node_l || node_r < l) return -INF;
        if (l <= node_l && node_r <= r) return max_tree[k];
        int mid = (node_l + node_r) / 2;
        return max(query_max(l, r, 2 * k, node_l, mid),
                   query_max(l, r, 2 * k + 1, mid + 1, node_r));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> P(N + 1);
    vector<int> pos(N + 1); 
    SegmentTree seg(N);

    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
        pos[P[i]] = i;
        seg.update(i, P[i]);
    }

    for (int i = 0; i < M; ++i) {
        int L, R;
        cin >> L >> R;

        int min_val = seg.query_min(L, R);
        int max_val = seg.query_max(L, R);

        if (min_val == max_val) continue;

        int idx_min = pos[min_val];
        int idx_max = pos[max_val];

        swap(P[idx_min], P[idx_max]);

        pos[min_val] = idx_max;
        pos[max_val] = idx_min;

        seg.update(idx_min, max_val);
        seg.update(idx_max, min_val);
    }

    for (int i = 1; i <= N; ++i) {
        cout << P[i] << (i == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}