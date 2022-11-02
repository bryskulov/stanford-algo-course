from argparse import ArgumentParser
from ast import literal_eval

def read_file(name):
    """Given the name of the file , return the graph in list.
    """
    graph = [0]
    
    file = open(name)
    data = file.readlines()
    for line in data:
        items = line.split()
        graph.append([literal_eval(a) for a in items[1:]])
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

def main(filename):
    G = read_file(filename)
    indices = [7,37,59,82,99,115,133,165,188,197]
    A = dijkstra(G, 1)
    distances = [A[i] for i in indices]
    result = [','.join(map(str, distances))]
    return result

if __name__ == '__main__':
    parser = ArgumentParser(description="Dijkstra shortest path filename")
    parser.add_argument("-i", dest="filename", required=True,
                        help="input txt file of the graph", metavar="FILE")
    args = parser.parse_args()
    print(main(args.filename))