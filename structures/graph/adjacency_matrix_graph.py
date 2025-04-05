class UnweightedGraph:
    """
    Description: Unweighted graph using adjacency matrix.
    Time complexity: O(1)
    Space complexity: O(n^2)
    """
    def __init__(self, n: int):
        self.adj = [[False] * n for _ in range(n)]

    def add_edge(self, u: int, v: int, directed: bool = False) -> None:
        self.adj[u][v] = True
        if not directed:
            self.adj[v][u] = True

    def remove_edge(self, u: int, v: int, directed: bool = False) -> None:
        self.adj[u][v] = False
        if not directed:
            self.adj[v][u] = False

    def has_edge(self, u: int, v: int, directed = False) -> bool:
        return self.adj[u][v] or not directed and self.adj[v][u]


class WeightedGraph:
    """
    Description: Weighted graph using adjacency matrix.
    Time complexity: O(1)
    Space complexity: O(n^2)
    """
    def __init__(self, n: int):
        self.adj = [[0] * n for _ in range(n)]

    def add_edge(self, u: int, v: int, weight: int = 1, directed: bool = False):
        self.adj[u][v] = weight
        if not directed:
            self.adj[v][u] = weight

    def remove_edge(self, u: int, v: int, directed: bool = False):
        self.adj[u][v] = 0
        if not directed:
            self.adj[v][u] = 0

    def has_edge(self, u: int, v: int, directed = False) -> bool:
        return self.adj[u][v] != 0 or not directed and self.adj[v][u] != 0
