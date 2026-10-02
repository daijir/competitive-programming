// https://atcoder.jp/contests/abc476/tasks/abc476_b

#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    string S, T;
    if (!(cin >> N >> S >> T)) return 0;

    for (int i = 0; i < N; ++i) {
        if (T[i] != '*' && S[i] != T[i]) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}