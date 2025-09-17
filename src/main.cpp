#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<int> v = {3, 1, 2};
  for (auto x : v) {
    cout << x << " ";
  }
  cout << endl;
}
