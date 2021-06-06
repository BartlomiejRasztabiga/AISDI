import heapq
import sys
from math import inf
from typing import Tuple, Dict, List

# typedef
Point = Tuple[int, int]
QueueElement = Tuple[Point, float, List[Point]]  # (point, cost, route)


class NoStartOrEndNode(ValueError):
    def __init__(self):
        super().__init__("Given graph does not have both start and end nodes")


class NoPathExists(ValueError):
    def __init__(self):
        super().__init__("No path between given points exists")


class Graph(Dict[Point, int]):
    def init_from_matrix(self, matrix):
        """
        Creates a graph from a 2D array.

        Every character of that file represents a point on a Graph.
        If that char is a digit - it represents node with given weight.
        """
        for y, row in enumerate(matrix):
            for x, char in enumerate(row):
                self[x, y] = int(char)

    def costs_for_path(self, path: List[Point]):
        """
        Returns a dictionary with weights of given Points.
        """
        costs: Dict[Point, int] = {}

        for point in path:
            costs[point] = self[point]
        return costs

    def shortest_path(self) -> List[Point]:
        """
        Finds the shortest path between points with weight 0
        using Dijkstra's algorithm.

        Raises:
        - NoPathExists if no path between given points is found
        """

        start, end = self._start_and_end_nodes()
        costs: Dict[Point, float] = {start: 0}
        queue: List[QueueElement] = [(start, 0, [start])]

        while queue:
            # get next point from queue
            point, cost, path = heapq.heappop(queue)

            # ignore if we already have a better path
            if cost > costs.get(end, inf):
                continue

            # return if complete path is found
            if point == end:
                return path

            # check cost of route through neighbours
            for neighbour, additional_cost in self._neighbours(point):
                neighbour_cost = cost + additional_cost

                # if this route is better than any found earlier, push it to the queue
                if neighbour_cost < costs.get(neighbour, inf):
                    costs[neighbour] = neighbour_cost
                    heapq.heappush(queue, (neighbour, neighbour_cost, path + [neighbour]))

        # end never reached - no possible path exists
        raise NoPathExists()

    def _possible_neighbours(self, point: Point) -> List[Point]:
        """
        Returns all possible neighbours of a Point in Graph.
        """
        x, y = point
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def _neighbours(self, point: Point) -> List[Tuple[Point, int]]:
        """
        Returns all existing neighbours of a Point in Graph with weights.
        """
        return [(neighbour, self[neighbour]) for neighbour in self._possible_neighbours(point) if neighbour in self]

    def _start_and_end_nodes(self) -> List[Point]:
        """
        Returns start and end nodes (weight == 0)
        """
        nodes = [point for (point, weight) in self.items() if weight == 0]
        if len(nodes) != 2:
            raise NoStartOrEndNode()
        return nodes


def prettify_path(path: List[Point], costs: Dict[Point, int]) -> str:
    width = max(point[0] for point in path) + 1
    height = max(point[1] for point in path) + 1
    chars = [[" "] * width for _ in range(height)]

    for point in path:
        chars[point[1]][point[0]] = str(costs[point])

    return "\n".join("".join(row) for row in chars)


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
