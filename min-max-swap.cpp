// https://atcoder.jp/contests/abc476/tasks/abc476_e

// がんばるぞ

#include <atcoder/all>

// ✔ AtCoder が公式に配布している「競プロ用ライブラリ」を全部読み込むヘッダ
// <atcoder/all> を読み込むと、ACL のすべての機能が使えるようになる。

// segtree（セグメントツリ), fenwick_tree（BIT）, dsu（Union-Find）, modint（MOD 計算）, lazy_segtree（遅延セグ木）, mf_graph（最大流）, scc_graph（強連結成分分解）, などなど

#include <bits/stdc++.h>

// GCC が内部で持っている「全部入りヘッダ」
// <bits/stdc++.h> は GCC（GNU g++）だけが持っている非標準ヘッダ。
// これを読み込むと：<iostream>, <vector>, <algorithm>, <map>, <set>, <queue>
// …などなど
// ほぼ全部の標準ライブラリが一気に読み込まれる。

using namespace std;

// 型エイリアス（alias）
using S = pair<int, int>;

// operator と identity element を定義する
// op（operation）→「2つの値をどう合成するか（親ノードをどう作るか）」
// e（identity element）→「単位元（初期値）」

S op_max(S a, S b) { return a.first > b.first ? a : b; }
S e_max() { return {-1, -1}; }
S op_min(S a, S b) { return a.first < b.first ? a : b; }
S e_min() { return {INT_MAX, -1}; }

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N, M;
	cin >> N >> M;
	vector<int> P(N);
	for (int &x : P) cin >> x;
	vector<S> A(N);
	for (int i = 0; i < N; i++) A[i] = {P[i], i};
	atcoder::segtree<S, op_max, e_max> seg_max(A);
	atcoder::segtree<S, op_min, e_min> seg_min(A);

	while (M--) {
		int L, R;
		cin >> L >> R;
		L--;
		const auto [mx, i] = seg_max.prod(L, R);
		const auto [mn, j] = seg_min.prod(L, R);
		swap(P[i], P[j]);
		seg_max.set(i, {P[i], i});
		seg_max.set(j, {P[j], j});
		seg_min.set(i, {P[i], i});
		seg_min.set(j, {P[j], j});
	}

	for (int i = 0; i < N; i++) {
		cout << P[i] << " \n"[i + 1 == N];
	}
}