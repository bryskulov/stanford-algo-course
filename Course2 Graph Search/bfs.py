class graph:

    def __init__(self, G):
        self.G = G
        self.global_explored = list()

    def bfs(self, s):
        """
        Output: 
            Graph with all vertices reachable from s explored.
        """
        self.s = s
        explored = [s]
        Q = [self.s]
        while len(Q) != 0:
            v = Q.pop()
            for w in self.G[v]:
                if w not in explored:
                    explored.append(w)
                    Q.append(w)
        G_out = dict((k, self.G[k]) for k in explored)
        self.global_explored = self.global_explored + explored
        return G_out

    def shortest_path(self, s):
        """
        Output: 
            dist(v) for any vertex v, i.e. min number of edges on a path from s to v
        """
        self.s = s
        dist = dict.fromkeys(self.G.keys(), float('inf'))
        dist[self.s] = 0
        explored = list(self.s)
        Q = [self.s]
        while len(Q) != 0:
            v = Q.pop()
            for w in self.G[v]:
                if w not in explored:
                    explored.append(w)
                    dist[w] = dist[v] + 1
                    Q.append(w)
        return dist

    def undir_con_comp(self):
        """
            Connected components of G
        """
        self.global_explored = list()
        connected_components = list()
        for i in range(len(self.G)):
            if str(i+1) not in self.global_explored:
                component = self.bfs(str(i+1))
                connected_components.append(component)
        return connected_components