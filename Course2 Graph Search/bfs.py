def bfs(G, s):
    """
    Input"
        G: Graph with all vertices unexplored
        s: Source vertex s
    Output: 
        Graph with all vertices reachable from s explored.
    """
    explored = list(s)
    Q = list(s)
    while len(Q) != 0:
        v = Q.pop()
        for w in G[v]:
            if w not in explored:
                explored.append(w)
                Q.append(w)
    G_out = dict((k, G[k]) for k in explored)
    return G_out


def shortest_path(G, s):
    """
    Input"
        G: Graph with all vertices unexplored
        s: Source vertex s
    Output: 
        dist(v) for any vertex v, i.e. min number of edges on a path from s to v
    """
    dist = dict.fromkeys(test.keys(), float('inf'))
    dist[s] = 0
    explored = list(s)
    Q = list(s)
    while len(Q) != 0:
        v = Q.pop()
        for w in G[v]:
            if w not in explored:
                explored.append(w)
                dist[w] = dist[v] + 1
                Q.append(w)
    return dist


def undir_con_comp(G):
    """
    Input"
        G: Undirected graph G with all vertices unexplored and labeled 1 to n
    Output:
        Connected components of G
    """
    connected_components = list()
    for i in range(len(G)):
        component = bfs(G, str(i+1))
        connected_components.append(component)
    return connected_components


test = dict({'1': ['2', '3', '4', '5'],
            '2': '1',
            '3': '1',
            '4': '1',
            '5': ['1', '6', '7'],
            '6': ['5'],
            '7': '5',
            '8': ''})

print(bfs(test, '1'))
print(shortest_path(test, '1'))
print(undir_con_comp(test))