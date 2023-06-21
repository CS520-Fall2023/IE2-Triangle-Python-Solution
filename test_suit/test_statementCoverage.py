import unittest
from isTriangle import Triangle

class StatementCoverageTest(unittest.TestCase):

    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(expected, actual)

    def test2(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(expected, actual)

    def test3(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(expected, actual)

    def test4(self):
        actual = Triangle.classify(1, 2, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(expected, actual)

    def test5(self):
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(expected, actual)

    def test6(self):
        actual = Triangle.classify(3, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(expected, actual)

    def test7(self):
        actual = Triangle.classify(2, 3, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(expected, actual)

    def test8(self):
        actual = Triangle.classify(2, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(expected, actual)
