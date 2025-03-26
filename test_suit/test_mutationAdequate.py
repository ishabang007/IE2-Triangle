import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    def test_scalene_triangle(self):
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        result = Triangle.classify(4, 4, 4)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    def test_isosceles_triangle(self):
        result = Triangle.classify(3, 3, 4)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_invalid_triangle(self):
        result = Triangle.classify(1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_zero_size(self):
        result = Triangle.classify(0, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_negative_side(self):
        result = Triangle.classify(-1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_isosceles_invalid(self):
        result = Triangle.classify(5, 5, 10)
        self.assertEqual(result, Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()
