#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int st_player;
    cin >> st_player;
    
    vector<pair<int, int>> even, odd;
    int i;
    for (i = 0; i < 9; i++)
    {
        pair<int, int> pr;
        cin >> pr.first >> pr.second;
        vector<pair<int, int>>& ref= (i % 2) ? odd : even;
        ref.push_back(pr);
        
        int h_cnt, v_cnt, d_cnt, d2_cnt;
        h_cnt = count_if(ref.begin(), ref.end(), [&pr](pair<int, int> t) -> bool { return t.first == pr.first; });
        v_cnt = count_if(ref.begin(), ref.end(), [&pr](pair<int, int> t) -> bool { return t.second == pr.second; });
        d_cnt = count_if(ref.begin(), ref.end(), [&pr](pair<int, int> t) -> bool { return t.first == t.second; });
        d2_cnt = count_if(ref.begin(), ref.end(), [&pr](pair<int, int> t) -> bool { return t.first + t.second == 4; });


        if (h_cnt == 3 || v_cnt == 3 || d_cnt == 3 || d2_cnt == 3)
            break;
    }
    if (st_player % 2)
    {
        if (i % 2 == 0)
            cout << 1;
        else 
            cout << 2;
    }
    else 
    {
        if (i % 2 == 0)
            cout << 2;
        else 
            cout << 1;
    }

    // if (( st_player % 2 && i % 2 == 0 ) || ( st_player % 2 == 0 && i % 2 )) cout << 1;
    // else cout << 2;
}