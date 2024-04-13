#include<iostream>
using namespace std;

int main()
{
    int n, l;
    cin >> n >> l;

    int a[n];
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        if (a[i] >= l) {
            cnt++ ;
        }
    }
    cout << cnt << endl;

    return 0;
}
