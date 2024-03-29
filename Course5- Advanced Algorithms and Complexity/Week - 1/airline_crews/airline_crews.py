# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.parents = [-1 for i in range(n)]
        self.parents[0] = -2

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def find_path(graph,parents,M):
    max_distance = graph.size() + 2
    dist = [max_distance for _ in range(graph.size())]
    queue = [0]
    dist[0] = 0
    vertices = []
    while(len(queue)>0):
        u = queue.pop(0)
        for v_id in graph.graph[u]:
            v = graph.get_edge(v_id)
            if (parents[v.v] == -1 and v.capacity-v.flow > 0):
                parents[v.v] = v_id
                M[v.v] = min(M[u],v.capacity-v.flow)
                if v.v!=graph.size()-1:
                    queue.append(v.v)
                else:
                    return M[graph.size()-1],parents
    return 0,parents


def max_flow(graph,n):
    # your code goes here
    flow = 0
    final_matching = [-1] * n
    while True:
        parents = [-1 for i in range(graph.size())]
        parents[0] = -2
        M = [0 for i in range(graph.size())]
        M[0] = float('inf')
        new_flow, parents = find_path(graph, parents, M)
        if new_flow == 0:
            return final_matching
        flow += new_flow
        v = graph.size() - 1
        pathMatchings=[]
        while v != 0:
            pathMatchings.append(v)
            v_id = parents[v]
            graph.add_flow(v_id, new_flow)
            u_edge = graph.get_edge(v_id)
            v = u_edge.u
        for i in range(1,len(pathMatchings),2):
            match = pathMatchings[i:i+2]
            final_matching[match[1]-1]=match[0]-n-1
    return final_matching


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def buildGraph(self,adj_matrix,n,m):

        vertices = []
        graphSize=n+m+2
        for i in range(1,n+1):
            vertices.append([0,i,1])
        for i in range(n):
            for j in range(m):
                if(adj_matrix[i][j]):
                    vertices.append([i+1, n+j+1,1])
        for j in range(1,m+1):
            vertices.append([n+j, graphSize-1,1])
        graph = FlowGraph(graphSize)
        for i in range(len(vertices)):
            u = vertices[i][0]
            v = vertices[i][1]
            capacity = vertices[i][2]
            graph.add_edge(u, v, capacity)
        return graph

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        self.buildGraph(adj_matrix)
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        # matching = self.find_matching(adj_matrix)
        graph = self.buildGraph(adj_matrix, n, m)
        self.write_response(max_flow(graph,n))

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
