import bfs

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
G = bfs.graph(test_graph)

def test_bfs():
    actual_result = G.bfs('1')
    expected_result = {'1': ['2', '3', '4', '5'], '2': '1', '3': '1', '4': '1', '5': ['1', '6', '7'], '6': ['5'], '7': '5'}
    assert actual_result == expected_result

def test_shortest_path():
    actual_result = G.shortest_path('1')
    print(actual_result)
    expected_result = {'1': 0, '2': 1, '3': 1, '4': 1, '5': 1, '6': 2, '7': 2, 
                        '8': float('inf'), '9': float('inf'), '10': float('inf')}
    assert actual_result == expected_result

def test_undir_con_comp():
    actual_result = G.undir_con_comp()
    expexted_result = [{'1': ['2', '3', '4', '5'], '2': '1', '3': '1', '4': '1', '5': ['1', '6', '7'], '6': ['5'], '7': '5'}, {'8': '9', '9': '8'}, {'10': []}]
    assert actual_result == expexted_result