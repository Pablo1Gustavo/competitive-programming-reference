"""
Description: Pattern matching using FFT-based convolution, supporting wildcard '?' in the pattern.
Time complexity: O(n log n)
Space complexity: O(n)
Where n = len(text) + len(pattern)
"""

from math_and_number_theory.polynomial_multiplication import multiply

def fft_match(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    size = 2 ** (n + m - 1).bit_length()
    total = [0] * size

    pattern_alphabet = set(pattern) - {'?'}
    required = sum(c != '?' for c in pattern)

    for c_pattern in pattern_alphabet:
        A = [int(c == c_pattern) for c in text] + [0] * (size - n)
        B = [int(c == c_pattern) for c in reversed(pattern)] + [0] * (size - m)
        conv = multiply(A, B)

        for i in range(size):
            total[i] += conv[i]

    return [i for i in range(n - m + 1) if total[i + m - 1] == required]
