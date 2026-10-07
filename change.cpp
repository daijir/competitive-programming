#include<bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin >> n;

  int c1=0,c10=0,c100=0;
  for(int i=0;i<n;i++){
    int a;
    cin >> a;
    int x=(a+999)/1000*1000-a;
    c100+=x/100;
    c10+=x/10%10;
    c1+=x%10;
  }
  cout << c1 << ' ' << c10 << ' ' << c100 << endl;
}
