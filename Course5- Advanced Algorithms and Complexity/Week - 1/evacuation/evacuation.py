# python3
import time

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

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

    def print_edge(self,id):
        edge = self.edges[id]
        print("("+str(edge.u)+","+str(edge.v)+","+str(edge.capacity)+","+str(edge.flow)+")")

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def read_data_from_file(data):
    vertex_count = data[0][0]
    edge_count = data[0][1]
    graph = FlowGraph(vertex_count)
    for i in range(edge_count):
        u = data[1][i][0]
        v = data[1][i][1]
        capacity = data[1][i][2]
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def construct_path(dist_array,min_dist):
    path = []
    for i in range(min_dist,-1,-1):
        path.append(dist_array.index(i))
    return path

def find_path(graph):
    max_distance = graph.size() + 2
    dist = [max_distance for _ in range(graph.size())]
    queue = [0]
    dist[0] = 0
    vertices = []
    while(len(queue)>0):
        # print("Queue(before pop) ->", end=" ")
        # print(queue)
        u = queue.pop(0)

        for v_id in graph.graph[u]:
            v = graph.get_edge(v_id)
            # graph.print_edge(v_id)
            if (dist[v.v]==max_distance and v.capacity>0 and v.capacity-v.flow > 0):
                if not(len(vertices)>0 and vertices[-1]==u):
                    vertices.append((u))
                queue.append(v.v)
                # print("Queue ->", end=" ")
                # print(queue)
                # print("Dist ->", end=" ")
                # print(dist)
                dist[v.v]=dist[u]+1
                if(v.v==graph.size()-1):
                    vertices.append(v.v)
                    return(vertices)
    return []

def get_min_capacity(graph,path):
    min = float('inf')
    id = -1
    edges = []
    for i in range(0,len(path)-1):
        ids = graph.get_ids(path[i])
        for e_id in ids:
            edge = graph.get_edge(e_id)
            if edge.v == path[i+1] and edge.capacity>0 and edge.capacity-edge.flow > 0 :
                edges.append(e_id)
                if min > edge.capacity :
                    min = edge.capacity
                    id = e_id
    graph.add_flow(id,min)
    return (min,edges)

def max_flow(graph, from_, to):
     # your code goes here
    capacity = 0
    while True:
        path = find_path(graph)
        if len(path) == 0:
            return capacity
        (min_c,edges) = get_min_capacity(graph,path)
        capacity+=min_c
    return capacity



if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
