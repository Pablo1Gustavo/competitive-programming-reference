from math import isqrt

def is_prime(x: int) -> bool:
    """
    Description: Check if a number is prime using trial division up to sqrt(n).
    Time complexity: O(sqrt(n))
    Space complexity: O(1)
    """
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def is_prime2(x: int) -> bool:
    """
    Description: Optimized primality test using 6k ± 1 optimization.
    Time complexity: O(sqrt(n))
    Space complexity: O(1)
    """
    if x < 2 or x % 2 == 0:
        return x == 2
    if x % 3 == 0:
        return x == 3
    for i in range(5, isqrt(x) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True