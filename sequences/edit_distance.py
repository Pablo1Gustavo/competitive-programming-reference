"""
Description: Recursive Levenshtein distance (edit distance) with memoization (DP).
Time complexity: O(nm)
Space complexity: O(nm)
Where n = len(a), m = len(b)
"""

from functools import cache

@cache
def edit_distance(a: str, b: str, len_a: int, len_b: int) -> int:
    if len_a == 0:
        return len_b
    if len_b == 0:
        return len_a
    if a[len_a - 1] == b[len_b - 1]:
        return edit_distance(a, b, len_a - 1, len_b - 1)
    return 1 + min(
        edit_distance(a, b, len_a, len_b - 1),
        edit_distance(a, b, len_a - 1, len_b),
        edit_distance(a, b, len_a - 1, len_b - 1))

