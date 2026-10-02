// https://atcoder.jp/contests/abc476/tasks/abc476_c

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<int> top3 = {A[0], A[1], A[2]};
    sort(top3.begin(), top3.end());

    cout << top3[0] << "\n";

    for (int i = 3; i < N; ++i) {
        if (A[i] > top3[0]) {
            top3[0] = A[i];
            sort(top3.begin(), top3.end());
        }
        cout << top3[0] << "\n";
    }

    return 0;
}