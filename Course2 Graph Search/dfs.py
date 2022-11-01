# Slower dictionary implementation of DFS algorithm

class graph:

    def __init__(self, G):
        self.G = G
        self.explored = list()
        self.n_vertices = len(G)

    def dfs_ts(self, s):
        """
        Output: 
            Graph with all vertices reachable from s explored.
        """
        self.s = s
        self.explored.append(s)
        for v in self.G[s]:
            if v not in self.explored:
                self.dfs_ts(v)
        G_out = dict((k, self.G[k]) for k in self.explored)
        self.sorting[s] = self.current_label
        self.current_label -= 1
        return G_out

    def topological_sort(self):
        """
        Input"
            G: Directed acyclic graph G with n nodes
        Output:
            Topological ordering of G
        """
        self.explored = list()
        self.current_label = len(self.G)
        self.sorting = dict((k, self.G[k]) for k in self.G)
        for vertex in self.G.keys():
            if vertex not in self.explored:
                self.dfs_ts(vertex)
        return self.sorting

    def compute_scc(self):
        """
            Computes the strongly connected components for a directed graph
            Output:
                dictionary where key indicates a node and value corresponds to the SCC
        """
        
        self.dfs_loop_scc(loop='first')
        self.dfs_loop_scc(loop='second')
        return self.leader

    def dfs_loop_scc(self, loop='first'):
        self.reverse_graph()
        self.explored = list()
        if loop == 'first':
            self.finish_time = [None] * self.n_vertices
            self.t = 0
            for i in range(self.n_vertices, 0, -1) :
                if str(i) not in self.explored:
                    self.current_leader = str(i)
                    self.dfs_scc(str(i), loop='first')
        else:
            self.current_leader = None
            self.leader = dict.fromkeys(self.G.keys(), [])
            for num in range(self.n_vertices, 0, -1) :
                i = self.finish_time.index(num) + 1
                if str(i) not in self.explored:
                    self.current_leader = str(i)
                    self.dfs_scc(str(i), loop='second')

    def dfs_scc(self, s, loop):
        """
        Output: 
            Graph with all vertices reachable from s explored.
        """
        self.explored.append(s)
        if loop == 'second':
            self.leader[s] = self.current_leader
        for v in self.G[s]:
            if v not in self.explored:
                self.dfs_scc(v, loop)
        if loop == 'first':
            self.t += 1
            self.finish_time[int(s)-1] = self.t
        return

    def reverse_graph(self):
        """
            Reverses the directed graph
        """
        G_rev = dict.fromkeys(self.G.keys(), [])
        for v in self.G:
            for w in self.G[v]:
                G_rev[w] = G_rev[w] + [v]
        self.G = G_rev
        return