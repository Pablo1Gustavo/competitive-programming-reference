class UnweightedGraph:
    """
    Description: Unweighted graph using edge list representation.
    Time complexity: O(1)
    Space complexity: O(E)
    Where E = len(edges)
    """
    def __init__(self, n: int):
        self.n = n
        self.edges = set()

    def add_edge(self, u: int, v: int, directed: bool = False):
        self.edges.add((u, v))
        if not directed:
            self.edges.add((v, u))

    def remove_edge(self, u: int, v: int, directed: bool = False):
        self.edges.discard((u, v))
        if not directed:
            self.edges.discard((v, u))

    def has_edge(self, u: int, v: int, directed: bool = False):
        return (u, v) in self.edges or not directed and (v, u) in self.edges


class WeightedGraph:
    """
    Description: Weighted graph using edge list representation.
    Time complexity: O(E)
    Space complexity: O(E)
    Where E = len(edges)
    """
    def __init__(self):
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int, directed: bool = False):
        self.edges.append((u, v, weight))
        if not directed:
            self.edges.append((v, u, weight))

    def remove_edge(self, u: int, v: int, directed: bool = False):
        self.edges = [
            (x, y, w)
            for x, y, w in self.edges
            if (x, y) != (u, v) and (directed or (x, y) != (v, u))
        ]

    def has_edge(self, u: int, v: int, directed: bool = False):
        return (u, v) in self.edges or not directed and (v, u) in self.edges
