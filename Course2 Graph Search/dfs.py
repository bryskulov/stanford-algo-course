# def dfs(G, s):
#     """
#     Input:
#         G: Graph with all vertices unexplored
#         S: Source vertex s
#     Output:
#         G: Graph with all vertices reachable from s explored.
#     """
#     explored = [s]
#     for v in G[s]:
#         if v not in explored:
#             dfs(G, v)
#     G_out = dict((k, self.G[k]) for k in explored)
#     return G_out


class graph:

    def __init__(self, G):
        self.G = G
        self.explored = list()

    def dfs(self, s):
        """
        Output: 
            Graph with all vertices reachable from s explored.
        """
        self.s = s
        self.explored.append(s)
        for v in self.G[s]:
            if v not in self.explored:
                self.dfs(v)
        G_out = dict((k, self.G[k]) for k in self.explored)
        return G_out

test_graph = dict({'1': ['2', '3', '4', '5'],
            '2': '1',
            '3': '1',
            '4': '1',
            '5': ['1', '6', '7'],
            '6': ['5'],
            '7': '5',
            '8': '9',
            '9': '8',
            '10': []})
G = graph(test_graph)
print(G.dfs('8'))
