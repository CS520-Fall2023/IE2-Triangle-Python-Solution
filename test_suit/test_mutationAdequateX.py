import unittest
import sys
from isTriangle import Triangle

class MutationAdequateTestSuite(unittest.TestCase):
    # ------------------------ for mutant 20 ------------
    def test20(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 16 and 17 ------------
    def test1617(self):
        actual = Triangle.classify(1, 1, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 2, 3, 13 and 22 ------------
    def test5(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 4 ------------
    def test6(self):
        actual = Triangle.classify(-1, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 7, 8 and 12 ------------
    def test7(self):
        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 9 ------------
    def test8(self):
        actual = Triangle.classify(1, -1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 1, 6 and 15 ------------
    def test9(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 59 ------------
    def test67(self):
        actual = Triangle.classify(2, 3, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 59 ------------
    def test74(self):
        actual = Triangle.classify(2, 6, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 80 ------------
    def test80(self):
        actual = Triangle.classify(4, 9, 6)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 59 ------------
    def test85(self):
        actual = Triangle.classify(6, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 109 ------------
    def test109(self):
        actual = Triangle.classify(1, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 126 ------------
    def test126(self):
        actual = Triangle.classify(1, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 143 ------------
    def test143(self):
        actual = Triangle.classify(2, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # ------------------------ for mutant 143 ------------
    def test142(self):
        actual = Triangle.classify(2, 2, 1)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test111(self):
        actual = Triangle.classify(sys.maxsize, 56, sys.maxsize)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test36(self):
        actual = Triangle.classify(8, 9, sys.maxsize)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test37(self):
        actual = Triangle.classify(sys.maxsize, sys.maxsize, sys.maxsize)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    # def test128(self):
    #     actual = Triangle.classify(56, sys.maxsize, sys.maxsize)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test21(self):
        actual = Triangle.classify(-sys.maxsize - 1, -sys.maxsize - 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
