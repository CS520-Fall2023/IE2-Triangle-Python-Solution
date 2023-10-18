import unittest
from isTriangle import Triangle

class DecisionCoverageTestSuite(unittest.TestCase):
    def test0(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test1(self):
        actual = Triangle.classify(-10, 20, 30)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(30, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(10, 22, 31)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(10, 10, 15)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(10, 10, 25)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(10, 15, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(15, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(10, 10, -10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(10, -20, 30)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(10, 20, 30)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(20, 30, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(10, 25, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test13(self):
        actual = Triangle.classify(25, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
