#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> v(n, 0), tmp(n, 0);
    for (int i = 0; i < n; i++)
    {
        if (i < 3) tmp[i] = 1;
        cin >> v[i];
    }
    int max = 0;
    do 
    {
        int sum = 0;
        for (int i = 0; i < n; i++)
            if (tmp[i]) 
                sum += v[i];
        if (sum <= m)
            max = std::max(max, sum);
    }
    while (next_permutation(v.begin(), v.end()));
    cout << max;
}