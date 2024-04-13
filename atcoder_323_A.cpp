#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;

    int cnt = 0;
    for (int i = 1; i < s.length(); i+=2) {
        if (s[i] == '0') {
            cnt++;
        }
    }
    if (cnt == 8) {
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }

    return 0;
}

