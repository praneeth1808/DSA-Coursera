#Uses python3

import sys

class Acyclicty:
    def read(self):
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        self.n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        self.CCs = [-1 for _ in range(self.n)]
        self.adj = [[] for _ in range(self.n)]
        self.orderStack=[]
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)

    def acyclic(self):
        for i in range(self.n):
            if (self.CCs[i] == -1):
                if (self.explore(i) == 1):
                    return 1
        return 0

    def isInStack(self,v):
        for i in self.orderStack:
            if(i==v):
                return 1
        return 0

    def explore(self,v):
        self.orderStack.append(v)
        for i in self.adj[v]:
            if (self.isInStack(i)==0):
                if (self.explore(i) == 1):
                    return 1
            else:
                return 1
        self.orderStack.pop()

if __name__ == '__main__':
    acyclicty=Acyclicty()
    acyclicty.read()
    print(acyclicty.acyclic())