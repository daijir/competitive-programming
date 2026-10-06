#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	cin >> s;
	int n = s.size();
	string t(2 * n - 1, ' ');

	for (int i = 0; i < n; i++) t[2 * i] = s[i];
	for (int i = 1; i < n; i++) t[2 * i - 1] = 'o';

	cout << t << endl;
}