#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, m, p;
    cin >> n >> m >> p;
    int cnt = 0;

    if (n > m && n < p) {
        cnt = 1;
    }
    else if (n > m && n > p) {
        for (int i = m; i <= n; i+=p) {
            cnt += 1;
        }
    }
    else if (n < m && n < p) {
        cnt = 0;
    }

    cout << cnt << endl;

    return 0;

}
