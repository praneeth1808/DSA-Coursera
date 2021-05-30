# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    # print("3 2")
    # print("1 2 0")
    # print("-1 -2 0")
    # print("1 -2 0")
    clauses=[]
    for i in range(n):
        clauses.append([(i * 3 + 1), (i * 3 + 2), (i * 3 + 3)])
        clauses.append([-1 * (i * 3 + 1), -1 * (i * 3 + 2)])
        clauses.append([-1 * (i * 3 + 1), -1 * (i * 3 + 3)])
        clauses.append([-1 * (i * 3 + 2), -1 * (i * 3 + 3)])
    for edge in edges:
        clauses.append([-1 * ((edge[0]-1) * 3 + 1), -1 * ((edge[1] -1)* 3 + 1)])
        clauses.append([-1 * ((edge[0]-1) * 3 + 2), -1 * ((edge[1] -1)* 3 + 2)])
        clauses.append([-1 * ((edge[0]-1) * 3 + 3), -1 * ((edge[1] -1)* 3 + 3)])
    print(len(clauses),end = " ")
    print(n*3)
    for clause in clauses:
        for i in clause:
            print(i,end=" ")
        print(0)

printEquisatisfiableSatFormula()

# print(n)
# print(m)
# print(edges)
