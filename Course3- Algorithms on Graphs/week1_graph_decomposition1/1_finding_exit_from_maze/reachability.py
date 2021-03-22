#Uses python3

import sys

def reach(visited,adj, x, y):
    if len(adj[x])==0:
        return 0
    for i in adj[x]:
        if i == y :
            return 1
    visited[x]=1
    for i in adj[x]:
        if(visited[i]==0):
            if reach(visited, adj, i, y) == 1:
                return 1
    return 0
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    visited=[0 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(visited,adj, x, y))
