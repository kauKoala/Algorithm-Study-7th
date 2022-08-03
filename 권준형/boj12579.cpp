#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> v(81);
    for (int i = 0; i < 81; i++)
        cin >> v[i];
    
    vector<int>::iterator max_iter = max_element(v.begin(), v.end());
    cout << *max_iter << "\n";
    int idx = max_iter - v.begin();
    cout << idx / 9  + 1 << " " << idx % 9 + 1 << "\n";
}