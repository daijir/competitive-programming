#include <iostream>
#include <string>

using namespace std;

int main() {
  string S;
  cin >> S;
  
  if (S.back() == 'e') {
    cout << S + "r" << endl;
  } else {
    cout << S + "er" << endl;
  }
  
  return 0;
}