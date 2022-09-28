import random, copy
from pathlib import Path


def search_min_cut(filename, n=20):
    """
    Input:
        filename: input file name
        n: the number of iterations/trials.

    Output:
        min_cut: the minimum cut
        
    """
    graph = transform_to_dict(filename)
    min_cut = 1000
    for i in range(n):
        G = copy.deepcopy(graph)
        cut = karger_mincut(G, choosen_seed=i)
        if cut < min_cut:
            min_cut = cut
    return min_cut


def karger_mincut(G, choosen_seed):
    """
    Input:
        G: G = (V,E) - an undirected graph in dictionary format (parallel edges are allowed).
    Output:
        num_edges: Number of crossing edges in a minimum cut
    """
    while len(G) > 2:
        #random.seed(choosen_seed)
        v, e_list = random.choice(list(G.items()))
        e = random.choice(e_list)
        e_merged = G.get(v) + G.get(e)

        if v in e_merged: 
            e_merged= list(filter((v).__ne__, e_merged))
        if e in e_merged: 
            e_merged =list(filter((e).__ne__, e_merged))

        G[v] = e_merged
        G.pop(e, None)

        for key in G:
            value = G.get(key)
            G[key] = list(map(lambda x: x if x != e else v, value))
    num_edges = len(G[next(iter(G))])
    return num_edges
    

def transform_to_dict(file_path):
    """
    Input:
        file_path: name of the file with adjacency list of the graph
    Output:
        G_dict: graph in dictionary format
    """
    G_dict = {}
    test_directory = Path(__file__).parent
    with open(test_directory / file_path, "r") as f_in:
        for line in f_in:
            parts = line.split()
            G_dict[parts[0]] = [x for x in parts[1:]]
    return G_dict


print(search_min_cut("tests/karger_graph.txt", 100))