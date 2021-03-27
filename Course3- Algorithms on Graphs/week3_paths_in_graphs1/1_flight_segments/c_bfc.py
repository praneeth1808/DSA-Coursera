import  sys

class BFS:
    def read(self):
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        self.n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        self.adj = [[] for _ in range(self.n)]
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)
            self.adj[b - 1].append(a - 1)
        self.s, self.t = data[2 * m] - 1, data[2 * m + 1] - 1
        self.max=self.n+1
        self.dist = [self.max for _ in range(self.n)]
        self.queue=[]

    def distance(self):
        self.dist[self.s]=0
        self.queue.append(self.s)
        while (len(self.queue)>0):
            u=self.queue.pop(0)

            for v in self.adj[u]:
                if(self.dist[v]==self.max):
                    self.queue.append(v)
                    self.dist[v]=self.dist[u]+1
                    if(v==self.t):
                        return self.dist[v]
        return -1


if __name__ == '__main__':
    bfs=BFS()
    bfs.read()
    print(bfs.distance())