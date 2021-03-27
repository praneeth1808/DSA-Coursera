import sys

class PriorityQueue:
    def __init__(self):
        self.size=-1
        self.heap=[]
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
        self.size = self.size + 1
        self.heap.append(p)
        self.shiftUp(self.size)
    def extractMin(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size = self.size - 1
        self.shiftDown(0)
        return result
    def isEmpty(self):
        return self.size==-1
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

if __name__ == '__main__':
    queue=PriorityQueue()
    queue.insert([0,7])
    queue.insert([1, 5])
    queue.insert([2, 3])
    print(queue.extractMin())
    queue.print()
    queue.insert([10, 9])
    queue.insert([9, 12])
    queue.print()
