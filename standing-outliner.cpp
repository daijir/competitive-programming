#include<bits/stdc++.h>
using namespace std;
int main(){
  int n, d; cin >> n >> d;
  vector<int> x(n);
  for (int i=0; i<n; i++) cin >> x[i];
  
  vector<int> p;
  for (int i=0; i<n; i++){
      bool ok = true;
      for (int j=0; j<n; j++){
          if (i != j){
              if (abs(x[i] - x[j]) < d) ok = false;
          }
      }
      if (ok) p.push_back(i + 1);
  }
  
  cout << p.size() << endl;
  for (auto e : p) cout << e << " ";
  cout << endl;
}
