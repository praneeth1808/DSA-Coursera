#Uses python3

import sys

class PriorityQueue:
    def __init__(self,heap):
        self.size=len(heap)-1
        self.heap=heap
        self.nodes=[]
    def isEmpty(self):
        return self.size==-1
    def parent(self,i):
        return (i - 1) // 2
    def leftChild(self,i):
        return ((2 * i) + 1)
    def rightChild(self,i):
        return ((2 * i) + 2)
    def shiftUp(self,i):
        while (i > 0 and self.heap[(i - 1) // 2][1] > self.heap[i][1]):
            self.swap((i - 1) // 2, i)
            i = (i - 1) // 2
    def shiftDown(self,i):
        maxIndex = i
        l = self.leftChild(i)
        if (l <= self.size and self.heap[l][1] < self.heap[maxIndex][1]):
            maxIndex = l
        r = self.rightChild(i)
        if (r <= self.size and self.heap[r][1] < self.heap[maxIndex][1]):
            maxIndex = r
        if (i != maxIndex):
            self.swap(i, maxIndex)
            self.shiftDown(maxIndex)
    def insert(self,p):
        self.nodes.append(p[0])
        self.size = self.size + 1
        self.heap.append(p)
        self.shiftUp(self.size)
    def extractMin(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size = self.size - 1
        self.shiftDown(0)
        return result

    def changePriority(self,v, p):
        i=-1
        for key,[u,d] in enumerate(self.heap):
            if(u==v):
                oldp = [u,d]
                i=key
        self.heap[i] = [v,p]
        if (p > oldp[1]):
            self.shiftUp(i)
        else:
            self.shiftDown(i)
    def swap(self,i,j):
        temp = self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
    def getMin(self):
        print(self.heap[0])
    def print(self):
        for [v,d] in self.heap[:self.size+1]:
            print(str(v)+"-"+str(d),end=" ; ")
        print("")

class Dijkstra:
    def read(self):
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        self.n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        self.adj = [[] for _ in range(self.n)]
        self.cost = [[] for _ in range(self.n)]
        for ((a, b), w) in edges:
            self.adj[a - 1].append(b - 1)
            self.cost[a - 1].append(w)
        self.s, self.t = data[0] - 1, data[1] - 1
        self.dist=[float("inf") for _ in range(self.n)]
        self.prev = [None for _ in range(self.n)]
        self.queue=PriorityQueue([[i,float("inf")] for i in range(self.n)])

    def distance(self):
        self.dist[self.s]=0
        self.queue.changePriority(self.s,0)
        while( not self.queue.isEmpty()):
            [u,dist]=self.queue.extractMin()
            for i,v in enumerate(self.adj[u]):
                if(self.dist[v]>dist+self.cost[u][i]):
                    self.dist[v]=dist+self.cost[u][i]
                    self.prev[v]=u
                    self.queue.changePriority(v,self.dist[v])
        return self.dist[self.t]


if __name__ == '__main__':
    dijkstra=Dijkstra()
    dijkstra.read()
    dist=dijkstra.distance()
    if(dist==float('inf')):
        print(-1)
    else:
        print(dist)