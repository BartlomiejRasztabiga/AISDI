from main import Graph, prettify_path


class TestInitGraphFromMatrix:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert len(graph) == 9
        assert graph[0, 0] == 1
        assert graph[1, 0] == 2
        assert graph[2, 0] == 4
        assert graph[0, 1] == 0
        assert graph[1, 1] == 6
        assert graph[2, 1] == 8
        assert graph[0, 2] == 4
        assert graph[1, 2] == 2
        assert graph[2, 2] == 0


class TestGraphPossibleNeighbours:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph._possible_neighbours((1, 1)) == [(0, 1), (2, 1), (1, 0), (1, 2)]


class TestGraphNeighbours:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph._neighbours((0, 0)) == [((1, 0), 2), ((0, 1), 0)]


class TestGraphStartEndNodes:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph._start_and_end_nodes() == [(0, 1), (2, 2)]


class TestGraphShortestPath:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "111122",
            "104122",
            "941111",
            "996411",
            "990411",
            "991111",
        ])
        expected_path = [
            (1, 1), (1, 2), (2, 2), (2, 3), (2, 4)
        ]

        assert graph.shortest_path() == expected_path


class TestGraphPathPrint:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "111122",
            "104122",
            "941111",
            "996411",
            "990411",
            "991111",
        ])
        path = graph.shortest_path()
        costs = graph.costs_for_path(path)
        expected_result = "\n".join([
            "   ",
            " 0 ",
            " 41",
            "  6",
            "  0",
        ])
        print(prettify_path(path, costs))
        assert prettify_path(path, costs) == expected_result