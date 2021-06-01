# python3

from collections import defaultdict

n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

class Graph:
    def __init__(self, literals):
        self.literals = literals
        self.V = literals*2 +1
        self.graph = defaultdict(list)
        self.sgc = []
        self.solution = [-1]*self.V

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addClause(self,u,v):
        self.addEdge(self.get_i_v(u),self.get_v(v))
        self.addEdge(self.get_i_v(v), self.get_v(u))

    def get_v(self,i):
        return self.literals+i
    def get_i_v(self,i):
        return self.literals+(-1*i)
    def get_l(self, i):
        return i - self.literals
    def get_i_l(self,i):
        return self.literals - i

    def assignVal(self,i,val):
        self.solution[i] = val
        if(i<self.literals):
            self.solution[self.literals+i+1] = (val+1)%2
        elif(i>self.literals):
            self.solution[i-self.literals -1] = (val + 1) % 2

    def DFSUtil(self, v, visited):
        visited[v] = True
        self.sgc[-1].append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):

        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            gr.sgc.append([])
            if visited[i] == False:
                gr.DFSUtil(i, visited)
        gr.sgc.reverse()
        return gr.sgc


# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable_naive():
    for mask in range(1<<n):
        print(mask)
        result = [ (mask >> i) & 1 for i in range(n) ]
        print(result)
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def isSatisfiable():
    g = Graph(n)
    for _ in clauses:
        g.addClause(_[0],_[1])
    SGCs = g.printSCCs()
    print(g.graph)
    print(SGCs)
    for sgc in SGCs:
        l = len(sgc)
        if (l > 1):
            for i in range(int(l / 2)):
                for j in range(i, l):
                    if (abs(sgc[i] - sgc[j] -1) == g.literals):
                        print("UNSATISFIABLE")
                        quit()
        for i in sgc:
            if(g.solution[i]==-1):
                g.assignVal(i,1)
    print("SATISFIABLE")
    solution = g.solution[g.literals+1:]
    i = 1
    for v in solution:
        print(i if v ==1 else -1*i , end = " ")
        i+=1
    print("")

isSatisfiable()
# result = isSatisfiable_naive()
# if result is None:
#     print("UNSATISFIABLE")
# else:
#     print("SATISFIABLE")
#     print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
