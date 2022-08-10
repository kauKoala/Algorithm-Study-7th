#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
typedef long long ll;
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k; cin >> n >> k;
    int pi; 
    vector<ll> v;
    for (int j = 0; j < n; j++)
    {
        cin >> pi;
        ll res = 0;
        for (int i = 0; i < pi; i++)
        {
            long long  x, y;
            cin >> x >> y;
            res = max(x*x + y*y, res);
        }
        v.push_back(res);
    }
    sort(v.begin(), v.end(), less<ll>());
    cout << v[k-1] << ".00";
}