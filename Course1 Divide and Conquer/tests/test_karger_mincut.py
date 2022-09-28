import karger_mincut


def test_karger_mincut():
    actual_result = karger_mincut.search_min_cut("tests/karger_test_graph.txt", 50)
    expected_result = 2
    assert actual_result == expected_result