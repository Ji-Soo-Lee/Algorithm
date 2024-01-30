// bfs

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int map[1001][1001] = {0, };
int visited[1001][1001] = {0, }; // white: 0, gray: 1, black: 2
int dist[1001][1001] = {-1, };
pair<int, int> dir[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // right, left, down, up

void bfs(const pair<int, int> &target);

int main() {
    // for faster io
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    int n, m, in;
    pair<int, int> target;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> in;
            if (in == 2) {target.first = i; target.second = j;}
            map[i][j] = in;
        }
    }
    
    bfs(target);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j] != 2 && map[i][j] == 1)
                dist[i][j] = -1;
            if (visited[i][j] != 2 && map[i][j] == 0)
                dist[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << dist[i][j] << " ";
        cout << "\n";
    }

    return 0;
}

void bfs(const pair<int, int> &target) {
    dist[target.first][target.second] = 0;
    visited[target.first][target.second] = 1;

    queue<pair<int, int>> q;
    pair<int, int> v;
    q.push(target); 

    while(!q.empty()) {
        pair<int, int> u = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            v = {u.first + dir[i].first, u.second + dir[i].second};
            if (visited[v.first][v.second] == 0 && map[v.first][v.second] == 1) {
                visited[v.first][v.second] = 1;
                dist[v.first][v.second] = dist[u.first][u.second] + 1;
                q.push(v);
            }
        }
        visited[u.first][u.second] = 2;
    }
}
