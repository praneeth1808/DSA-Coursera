import sys


class PriorityQueue:
    def read(self,V):
        self.size=-1
        self.V=[]
        for i in V:
            self.insert(i)

    def parent(self,i):
        return (i - 1) // 2

    def leftChild(self,i):
        return ((2 * i) + 1)

    def rightChild(self,i):
        return ((2 * i) + 2)

    def shiftUp(self,i):
        while (i > 0 and self.V[(i - 1) // 2] > self.V[i]):
            self.swap((i - 1) // 2, i)
            i = (i - 1) // 2

    def shiftDown(self,i):
        maxIndex = i
        l = self.leftChild(i)
        if (l <= self.size and self.V[l] < self.V[maxIndex]):
            maxIndex = l
        r = self.rightChild(i)
        if (r <= self.size and self.V[r] < self.V[maxIndex]):
            maxIndex = r
        if (i != maxIndex):
            self.swap(i, maxIndex)
            self.shiftDown(maxIndex)

    def insert(self,p):
        self.size = self.size + 1
        self.V.append(p)
        self.shiftUp(self.size)

    def extractMax(self):
        result = self.V[0]
        self.V[0] = self.V[self.size]
        self.size = self.size - 1
        self.shiftDown(0)
        return result

    def changePriority(self,i, p):
        oldp = self.V[i]
        self.V[i] = p
        if (p > oldp):
            self.shiftUp(i)
        else:
            self.shiftDown(i)
    def remove(self,i):
        self.V[i]=self.V[0]+1
        self.shiftUp(i)
        self.extractMax()
    def swap(self,i,j):
        temp = self.V[i]
        self.V[i]=self.V[j]
        self.V[j]=temp
    def getMax(self):
        print(self.V[0])
    def print(self):
        for i in self.V:
            print(i,end=" ")


queue=PriorityQueue()
queue.read([45,20,14,12,31,7,11,13,7])
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())
print(queue.extractMax())

