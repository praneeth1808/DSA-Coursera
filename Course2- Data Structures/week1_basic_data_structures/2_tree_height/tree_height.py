# python3

import sys
import threading


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;
    def compute_height_fast(self):
        heights=[0]*self.n
        for vertex in range(self.n):
            i=self.parent[vertex]
            height=1
            while i!=-1:
                if heights[i]!=0:
                    height+=heights[i]
                    break
                height+=1
                i=self.parent[i]
            while vertex!=-1 and heights[vertex]==0:
                heights[vertex]=height
                height-=1
                vertex=self.parent[vertex]
        return max(heights)

def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(tree.compute_height_fast())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
