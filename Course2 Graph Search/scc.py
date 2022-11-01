from collections import OrderedDict

class Graph:
    def __init__(self, num_nodes, filename):
        self.num_nodes = num_nodes
        self.filename = filename
        self.gr = [[] for i in range(self.num_nodes)]
        self.r_gr = [[] for i in range(self.num_nodes)]
        self.scc = [0] * self.num_nodes
        self.order = []

    def read_graph(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        for line in data:
            items = line.split()
            self.gr[int(items[0])] += [int(items[1])]
            self.r_gr[int(items[1])] += [int(items[0])]

    def dfs_first(self):

        visited = [False] * self.num_nodes
        stack = []

        for node in reversed(range(self.num_nodes)):
            if (not visited[node]):
                stack.append(node)

            while stack:
                s = stack[-1]
                visited[s] = True
                finish_flag = True

                for connected_node in self.r_gr[s]:
                    if (not visited[connected_node]):
                        finish_flag = False
                        stack.append(connected_node)

                if finish_flag == True:
                    stack.pop()
                    self.order.append(s)
        self.order = list(OrderedDict.fromkeys(self.order))

    def dfs_second(self):

        visited = [False] * self.num_nodes
        stack = []
        scc_idx = 0
        self.order.reverse()
        
        for node in self.order:

            if (not visited[node]):
                stack.append(node)

            while stack:
                s = stack.pop()               
                if (not visited[s]):
                    self.scc[node] += 1
                visited[s] = True

                for connected_node in self.gr[s]:
                    if (not visited[connected_node]):
                        stack.append(connected_node)

    def run(self):
        self.read_graph(self.filename)
        self.dfs_first()
        self.dfs_second()
        self.scc = self.scc[1:]
        self.scc.sort(reverse=True)
        scc_top5 = self.scc[:5]
        return scc_top5

G = Graph(875715, 'SCC.txt')
print(G.run())