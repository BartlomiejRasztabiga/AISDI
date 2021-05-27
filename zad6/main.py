import sys

# typedef
from typing import Tuple, Dict, List

Point = Tuple[int, int]


class NoStartOrEndNode(ValueError):
    def __init__(self):
        super().__init__("Given graph does not have both start and end nodes")


class NoRouteExists(ValueError):
    def __init__(self):
        super().__init__("No route exists")


class Graph(Dict[Point, int]):
    def init_from_matrix(self, matrix):
        """
        Creates a graph from a 2D array.

        Every character of that file represents a point on a Graph.
        If that char is a digit - it represents node with given weight.
        """
        for x, row in enumerate(matrix):
            for y, char in enumerate(row):
                self[x, y] = int(char)

    def possible_neighbours(self, point: Point) -> List[Point]:
        """
        Returns all possible neighbours of a Point in Graph.
        """
        x, y = point
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def neighbours(self, point: Point) -> List[Tuple[Point, int]]:
        """
        Returns all existing neighbours of a Point in Graph with weights.
        """
        return [(neighbour, self[neighbour]) for neighbour in self.possible_neighbours(point) if neighbour in self]

    def start_and_end_nodes(self) -> List[Point]:
        """
        Returns start and end nodes (weight == 0)
        """
        nodes = [point for (point, weight) in self.items() if weight == 0]
        if len(nodes) != 2:
            raise NoStartOrEndNode()
        return nodes

    def shortest_path(self, start: Point, end: Point) -> List[Point]:
        """
        Finds the shortest path between given points using the Dijkstra's algorithm.

        If path doesn't exist - raises NoRouteExists.
        If start or end are not present in the graph - raises KeyError.
        """
        pass


def prettify_path(path: List[Point]) -> str:
    pass


def main():
    if len(sys.argv) < 2:
        print("No file given.")
        exit(-1)
    else:
        filename = sys.argv[1]
        input_matrix = read_file(filename)
        graph = Graph()
        graph.init_from_matrix(input_matrix)


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    main()
