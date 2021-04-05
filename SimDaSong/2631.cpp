// boj 2631 줄세우기
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x, ans=0;
    vector<int> lis;

    cin >> n;

    lis.push_back(0);
    for (int i = 0; i < n; i++) {
        cin >> x;

        if (lis.back() < x) {
            lis.push_back(x);
            ans++;
        } else {
            vector<int>::iterator it = lower_bound(lis.begin(), lis.end(), x);
            *it = x;
        }
    }

    cout << n - ans;
}