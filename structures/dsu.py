"""
Description: Disjoint Set Union (Union-Find) with path compression and union by rank.
Time complexity:
- find: O(a(n)) amortized.
- join: O(a(n)) amortized.
where a is the inverse Ackermann function (near constant time).
Space complexity: O(n)
"""

class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
