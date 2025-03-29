"""
Description: Multiply two polynomials using FFT-based convolution.
Time complexity: O(n log n)
Space complexity: O(n)
Where n = len(poly1) + len(poly2)
"""

from .fft import fft

def multiply(poly1: list[int], poly2: list[int]) -> list[int]:
    n = 1
    while n < len(poly1) + len(poly2):
        n <<= 1

    fa = list(map(complex, poly1)) + [0] * (n - len(poly1))
    fb = list(map(complex, poly2)) + [0] * (n - len(poly2))

    fft(fa, invert=False)
    fft(fb, invert=False)

    for i in range(n):
        fa[i] *= fb[i]

    fft(fa, invert=True)

    result = [round(fa[i].real) for i in range(len(poly1) + len(poly2) - 1)]
    return result
