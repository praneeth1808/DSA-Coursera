# python3

import time

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    clauses = []
    for i in range(n):
        v_pos = [(i * n) + j for j in range(1, n + 1)]
        clauses.append(v_pos)
        for j in range(0, n):
            for k in range(j + 1, n):
                clauses.append([-1 * v_pos[j],-1 * v_pos[k]])

    for i in range(1, n + 1):
        pos_v = [(j * n) + i for j in range(n)]
        clauses.append(pos_v)
        for j in range(0, n):
            for k in range(j + 1, n):
                clauses.append([-1 * pos_v[j],-1 * pos_v[k]])
    edges_v = [[] for _ in range(n)]
    for edge in edges:
        edges_v[edge[0]-1].append(edge[1]-1)
        edges_v[edge[1]-1].append(edge[0]-1)
    for i in range(n):
        for j in range(n):
            if j not in edges_v[i] and (j != i):
                for k in range(1,n):
                    clauses.append(findVal(i,j,k))
    print(len(clauses) , end = " ")
    print(n*n)
    for clause in clauses:
        for v in clause:
            print(v,end=" ")
        print(0)
def findVal(i,j,k):
    return [-1 * ((i * n) + k), -1 * ((j * n) + k + 1)]

printEquisatisfiableSatFormula()
