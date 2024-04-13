#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, x;

    cin >> n >> x;

    int a[n];
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        if (a[i] <= x) {
            sum += a[i];
        }
    }

    cout << sum << endl;

    return 0;
}
