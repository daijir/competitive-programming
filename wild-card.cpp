#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    string s, t; cin >> s >> t;

    string ans = "Yes";
    for (int i = 0; i < n; i++) {
        if (t[i] != s[i] && t[i] != '*') {
            ans = "No";
        }
    }

    cout << ans << "\n";
}