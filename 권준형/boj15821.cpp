#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k; cin >> n >> k;
    int pi; 
    vector<long double> v;
    for (int j = 0; j < n; j++)
    {
        cin >> pi;
        vector<long double> tri;
        for (int i = 0; i < pi; i++)
        {
            int x, y;
            cin >> x >> y;
            long double res = sqrtl(x*x + y*y);
            tri.push_back(res);
        }
        v.push_back(*max_element(tri.begin(), tri.end()));
    }
    sort(v.begin(), v.end(), less<long double>());
    long double dist = v[k-1];
    long double res = dist * dist;
    cout << fixed;
    cout.precision(2);
    cout << res;
}