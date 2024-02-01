#include <iostream>
#include <vector>

using namespace std;

void makeArray(vector<int> &v, int idx, int n, int m);

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int n, m;
    vector<int> v;

    cin >> n >> m;

    for (int i = 1; i < n - m + 2; i++) {
        v = vector<int> {i};

        makeArray(v, i, n, m);
    }

    return 0;
}

void makeArray(vector<int> &v, int idx, int n, int m) {
    for (int i = idx + 1; i < n + 2; i++) {
        if (v.size() == m) {
            for (auto it = v.begin(); it != v.end(); it++) {
                cout << *it << " ";
            }
            cout << "\n";
            v.pop_back();
            break;
        }

        else if (i > n) {
            v.pop_back();
        }

        else if (v.size() != m) {
            v.push_back(i);
            makeArray(v, i, n, m);
        }
    }
}
