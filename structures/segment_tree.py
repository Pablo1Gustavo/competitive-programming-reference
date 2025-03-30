"""
Segment Tree implementation for range queries and point updates.
Supports any associative binary operation (e.g., min, max, sum, gcd) with an identity element.

Time complexity:
- build: O(n)
- update: O(log n)
- query: O(log n)
Space complexity: O(n)
"""

from typing import Callable, TypeVar

T = TypeVar('T')

class SegmentTree:
    def __init__(self, data: list[T], op: Callable[[T, T], T], identity: T):
        self.n = len(data)
        self.op = op
        self.id = identity
        self.tree = [identity] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data: list[T], node: int, l: int, r: int) -> None:
        if l == r:
            self.tree[node] = data[l]
            return
        
        mid = (l + r) // 2
        self._build(data, 2 * node + 1, l, mid)
        self._build(data, 2 * node + 2, mid + 1, r)
        
        self.tree[node] = self.op(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, index: int, value: T, node: int = 0, l: int = 0, r: int | None = None) -> None:
        if l == r:
            self.tree[node] = value
            return
        if r is None:
            r = self.n - 1

        mid = (l + r) // 2

        if index <= mid:
            self.update(index, value, 2 * node + 1, l, mid)
        else:
            self.update(index, value, 2 * node + 2, mid + 1, r)

        self.tree[node] = self.op(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, ql: int, qr: int, node: int = 0, l: int = 0, r: int | None = None) -> T:
        if r is None:
            r = self.n - 1
        if qr < l or ql > r:
            return self.id
        if ql <= l and r <= qr:
            return self.tree[node]
        
        mid = (l + r) // 2
        left = self.query(ql, qr, 2 * node + 1, l, mid)
        right = self.query(ql, qr, 2 * node + 2, mid + 1, r)

        return self.op(left, right)
