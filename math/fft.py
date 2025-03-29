import cmath

def bit_reverse_copy(a: list[complex]) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

def fft(a: list[complex], invert: bool) -> None:
    n = len(a)
    bit_reverse_copy(a)

    length = 2
    
    while length <= n:
        angle = 2 * cmath.pi / length * (-1 if invert else 1)
        wlen = cmath.exp(angle * 1j)
        for i in range(0, n, length):
            w = 1
            for j in range(length // 2):
                u = a[i + j]
                v = w * a[i + j + length // 2]
                a[i + j] = u + v
                a[i + j + length // 2] = u - v
                w *= wlen
        length <<= 1

    if invert:
        for i in range(n):
            a[i] /= n

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


print(multiply([1, 2, 3], [4, 5, 6]))