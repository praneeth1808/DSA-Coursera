import evacuation_1

for i in range(1,37):
    question =[[],[]]
    path = "./tests/" + str(i) if i >9 else "./tests/0" + str(i)
    solution = "./tests/" + str(i)+".a" if i >9 else "./tests/0" + str(i) + ".a"
    f = open(path, "r")
    question[0]=[int(i) for i in f.readline().strip().split(" ")]
    for _ in range(question[0][1]):
        edge = f.readline()
        edge_array = [int(i) for i in edge.strip().split(" ")]
        question[1].append(edge_array)
    f_sol = open(solution, "r")
    c_sol = int(f_sol.readline())
    graph = evacuation_1.read_data_from_file(question)
    capacity = evacuation_1.max_flow(graph, 0, graph.size() - 1)
    if(capacity!= c_sol):
        print("***Error*** : " + path)
        print(capacity)
        print(c_sol)
    # else:
    #     print("Success : " + path)