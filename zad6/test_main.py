from main import Graph


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
        assert graph[0, 1] == 2
        assert graph[0, 2] == 4
        assert graph[1, 0] == 0
        assert graph[1, 1] == 6
        assert graph[1, 2] == 8
        assert graph[2, 0] == 4
        assert graph[2, 1] == 2
        assert graph[2, 2] == 0


class TestGraphPossibleNeighbours:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph.possible_neighbours((1, 1)) == [(0, 1), (2, 1), (1, 0), (1, 2)]


class TestGraphNeighbours:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph.neighbours((0, 0)) == [((1, 0), 0), ((0, 1), 2)]


class TestGraphStartEndNodes:
    def test_simple(self):
        graph = Graph()
        graph.init_from_matrix([
            "124",
            "068",
            "420"
        ])

        assert graph.start_and_end_nodes() == [(1, 0), (2, 2)]
