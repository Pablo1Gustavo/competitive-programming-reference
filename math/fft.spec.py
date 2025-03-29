import unittest
from fft import *

class TestPolynomialMultiplication(unittest.TestCase):
    def test_very_basic(self):
        self.assertEqual(multiply([1], [1]), [1])
        self.assertEqual(multiply([1], [0]), [0])
        self.assertEqual(multiply([10], [20]), [200])
        self.assertEqual(multiply([123], [456]), [56088])

    def test_basic(self):
        self.assertEqual(multiply([1, 2, 3], [4, 5, 6]), [4, 13, 28, 27, 18])
        self.assertEqual(multiply([1, 2], [3, 4]), [3, 10, 8])
        self.assertEqual(multiply([10, 20, 30], [40, 50, 60]), [400, 1300, 2800, 2700, 1800])

    def test_zero_poly(self):
        self.assertEqual(multiply([0, 0, 0], [1, 2, 3]), [0, 0, 0, 0, 0])
        self.assertEqual(multiply([0], [0]), [0])
        self.assertEqual(multiply([1, 2, 3], [0]), [0, 0, 0])
        self.assertEqual(multiply([0], [1, 2, 3]), [0, 0 , 0])

    def test_different_sizes(self):
        self.assertEqual(multiply([2, 0, 3, 4], [1, 2]), [2, 4, 3, 10, 8])
        self.assertEqual(multiply([5, 1], [2]), [10, 2])
        self.assertEqual(multiply([2], [5, 1]), [10, 2])

    def test_negatives(self):
        self.assertEqual(multiply([3, -2, 5], [-1, 4]), [-3, 14, -13, 20])
        self.assertEqual(multiply([-1, -2], [-3, -4]), [3, 10, 8])
        self.assertEqual(multiply([1, -1], [1, -1]), [1, -2, 1])

    def test_large(self):
        SIZE = 10000
        a = [1] * SIZE
        b = [1] * SIZE
        expected = list(range(1, SIZE)) + [SIZE] + list(range(SIZE - 1, 0, -1))
        self.assertEqual(multiply(a, b), expected)

if __name__ == '__main__':
    unittest.main()
