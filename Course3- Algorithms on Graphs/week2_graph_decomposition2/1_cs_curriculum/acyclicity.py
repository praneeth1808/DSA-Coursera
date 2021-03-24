#Uses python3

import sys


def explore(v,rank):
    CCs[v]=rank
    print(adj)
    for i in adj[v]:
        if(CCs[i]!=rank):
            if(explore(i,rank)==1):
                return 1
        else:
            return 1


def acyclic(adj,n):
    rank=0
    for i in range(n):
        if(CCs[i]==-1):
            if(explore(i,rank)==1):
                return 1
        rank+=1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    global CCs
    CCs=[-1 for _ in range(n)]
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print("adj-1")
    print(adj)
    print(acyclic(adj,n))
