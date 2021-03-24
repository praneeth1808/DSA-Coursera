#Uses python3

import sys

class TopoSort:
    def read(self):
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        self.n, m = data[0:2]
        data = data[2:]
        self.edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        self.adj = [[] for _ in range(self.n)]
        for (a, b) in self.edges:
            self.adj[a - 1].append(b - 1)
        self.postOrder=""
        self.visited=[0 for _ in range(self.n)]

    def explore(self, v):
        self.visited[v]=1
        for i in self.adj[v]:
            if (self.visited[i] == 0):
                self.explore(i)
        self.postOrder=str(v+1) + " "+self.postOrder

    def dfs(self):
        self.read()
        for i in range(self.n):
            if(self.visited[i]==0):
                self.explore(i)
        pass

    def toposort(self):
        used = [0] * len(self.adj)
        order = []
        # write your code here
        return order
    def isInStack(self,v):
        for i in self.orderStack:
            if(i==v):
                return 1
        return 0



if __name__ == '__main__':
    toposort=TopoSort()
    toposort.dfs()
    print(toposort.postOrder)