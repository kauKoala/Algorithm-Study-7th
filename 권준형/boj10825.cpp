#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n; cin >> n;

    vector<vector<int>> arr(n, vector<int>(4, 0));
    vector<string> names(n);
    for (int i = 0; i < n; i++)
    {
        vector<int> v(4, 0);
        arr[i][0] = i;
        cin >> names[i] >> arr[i][1] >> arr[i][2] >> arr[i][3];
    }

    sort(arr.begin(), arr.end(), [&names] (vector<int>& v1, vector<int>& v2) -> bool {
    if (v1[1] == v2[1])
    {
        if (v1[2] == v2[2])
        {
            if (v1[3] == v2[3])
                return names[v1[0]] < names[v2[0]];
            else 
                return v1[3] > v2[3];
        }
        else 
            return v1[2] < v2[2];
    }
    else 
        return v1[1] > v2[1];
    });

    string res;
    for (vector<vector<int>>::size_type i = 0; i < arr.size(); i++)
        res += names[arr[i][0]] + "\n";
    cout << res;
}