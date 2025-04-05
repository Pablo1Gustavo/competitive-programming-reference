class WeightedGraph:
    """
    Description: Weighted graph using adjacency list.
    Time complexity: O(deg(u))
    Space complexity: O(V + E)
    Where V = number of vertices, E = number of edges
    """
    def __init__(self, n: int):
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, w: int = 1, directed: bool = False):
        self.adj[u].append((v, w))
        if not directed:
            self.adj[v].append((u, w))

    def remove_edge(self, u: int, v: int, directed: bool = False):
        self.adj[u] = [(x, w) for x, w in self.adj[u] if x != v]
        if not directed:
            self.adj[v] = [(x, w) for x, w in self.adj[v] if x != u]

    def has_edge(self, u: int, v: int, directed: bool = False):
        return any(x == v for x, _ in self.adj[u]) or not directed and any(x == u for x, _ in self.adj[v])


class UnweightedGraph:
    """
    Description: Unweighted graph using adjacency list.
    Time complexity: O(1)
    Space complexity: O(V + E)
    Where V = number of vertices, E = number of edges
    """
    def __init__(self, n: int):
        self.adj = [set() for _ in range(n)]

    def add_edge(self, u: int, v: int, directed: bool = False):
        self.adj[u].add(v)
        if not directed:
            self.adj[v].add(u)

    def remove_edge(self, u: int, v: int, directed: bool = False):
        self.adj[u].discard(v)
        if not directed:
            self.adj[v].discard(u)

    def has_edge(self, u: int, v: int, directed: bool = False):
        return v in self.adj[u] or not directed and u in self.adj[v]
