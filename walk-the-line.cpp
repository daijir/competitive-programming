#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll n, s, L;
    cin >> n >> s >> L;
    s--;
    vector<ll> a(n - 1);
    for (auto& e : a) cin >> e;
    int ans = 1;
    vector<ll> p(n);
    for (int i = 0; i < n - 1; i++) p[i + 1] = p[i] + a[i];
}