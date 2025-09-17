#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<int> nums = {5, 3, 8, 1, 2};
  sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
  for (auto n : nums) {
    cout << "Number: " << n << "\n";
  }
  cout << "Done!" << endl;
  return 0;
}
