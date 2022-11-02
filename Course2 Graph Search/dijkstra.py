from ast import literal_eval

def read_file(name, num_nodes):
    """Given the name of the file , return the graph in list.
    """
    graph = [None]*num_nodes
    
    file = open(name)
    data = file.readlines()
    for line in data:
        items = line.split()
        graph[int(items[0])] = [literal_eval(a) for a in items[1:]]
    graph[0] = [(0, 0)]

    return graph

def dijkstra(G, s):
    """
    Input:
        G: Undirected graph G(V;E). Each edge e 2 E has non-negative lengths le
        s: Source vertex
    Output
        Shortest path from s to v for all vertices
    """
    num_nodes = len(G)
    V = [i for i in range(num_nodes)]
    X = [s]

    A = [1000000] * num_nodes
    A[s] = 0

    while len(X) != num_nodes:
        min_distance = 1000000
        saved_w = 0
        for v in X:
            for w in G[v]:
                if (A[v] + w[1]) < min_distance and w[0] not in X:
                    min_distance = A[v] + w[1]
                    saved_w = w[0]
        X.append(saved_w)
        A[saved_w] = min_distance
    return A


G = read_file('dijkstraData.txt', 201)
indices = [7,37,59,82,99,115,133,165,188,197]
A = dijkstra(G, 1)
print([A[i] for i in indices])