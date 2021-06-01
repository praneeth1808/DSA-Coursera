#
# from collections import defaultdict
#
# class Graph:
#     def __init__(self, literals):
#         self.literals = literals
#         self.V = literals*2 +1
#         self.graph = defaultdict(list)
#         self.sgc = []
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def addClause(self,u,v):
#         self.addEdge(self.get_i_v(u),self.get_v(v))
#         self.addEdge(self.get_i_v(v), self.get_v(u))
#
#     def get_v(self,i):
#         return self.literals+i
#     def get_i_v(self,i):
#         return self.literals+(-1*i)
#     def get_l(self, i):
#         return i - self.literals
#     def get_i_l(self,i):
#         return self.literals - i
#
#     def DFSUtil(self, v, visited):
#         visited[v] = True
#         self.sgc[-1].append(v)
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.DFSUtil(i, visited)
#
#     def fillOrder(self, v, visited, stack):
#         visited[v] = True
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.fillOrder(i, visited, stack)
#         stack = stack.append(v)
#
#     def getTranspose(self):
#         g = Graph(self.V)
#
#         for i in self.graph:
#             for j in self.graph[i]:
#                 g.addEdge(j, i)
#         return g
#
#     def printSCCs(self):
#
#         stack = []
#         visited = [False] * (self.V)
#         for i in range(self.V):
#             if visited[i] == False:
#                 self.fillOrder(i, visited, stack)
#         gr = self.getTranspose()
#         visited = [False] * (self.V)
#
#         while stack:
#             i = stack.pop()
#             gr.sgc.append([])
#             if visited[i] == False:
#                 gr.DFSUtil(i, visited)
#         return gr.sgc
#
# # g = Graph(2)
# # g.addClause(1,1)
# # g.addClause(-1,-1)
#
# g = Graph(3)
# g.addClause(1,-3)
# g.addClause(-1,2)
# g.addClause(-2,-3)
#
# SGCs=g.printSCCs()
# for sgc in SGCs:
#     l = len(sgc)
#     if(l>1):
#         for i in range(int(l/2)):
#             for j in range(i,l):
#                 if(abs(sgc[i] - sgc[j]) == g.literals):
#                     print("UNSATISFIABLE")
#                     quit()
#
# print("SATISFIABLE")


[0 , 1, 2, 3, 4, 5, 6]
[-1,-1,-1,-1,-1,-1,-1]


