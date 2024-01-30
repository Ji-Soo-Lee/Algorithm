// dfs

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

map<int, vector<int>> tree;
int pred[100001] = {0,};
// white : 0, gray : 1, black : 2
int visited[100001] = {0,};

void dfs(int n, int u);

int main() {
    // for faster io
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    int n, a, b, root = 1;

    cin >> n;

    for (int i = 0; i < n-1; i++) {
        cin >> a >> b;

        if (tree.count(a) == 0)
            tree[a] = {b};
        else
            tree[a].push_back(b);

        if (tree.count(b) == 0)
            tree[b] = {a};
        else
            tree[b].push_back(a);
    }

    dfs(n, root);

    for (int i = 2; i < n+1; i++) {
        cout << pred[i] << "\n";
    }

    return 0;
}

void dfs(int n, int u) {
    visited[u] = 1;
    vector<int> adj = tree[u];

    for (int i = 0; i < adj.size(); i++) {
        if (visited[adj[i]] == 0) {
            pred[adj[i]] = u;
            dfs(n, adj[i]);
        }
    }
    visited[u] = 2;
}
