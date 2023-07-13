import unittest
from triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
