import unittest
from isTriangle import Triangle


class MutantAdequateTest(unittest.TestCase):

    def test_killMutant1(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_killMutant4(self):
        actual = Triangle.classify(-1, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant9(self):
        actual = Triangle.classify(10, -1, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test_killMutant11(self):
    #     actual = Triangle.classify((1 << 31) | 5, (1 << 31) | 6, 10)
    #     expected = Triangle.Type.INVALID
    #     print(actual, expected)
    #     self.assertEqual(actual, expected)

    def test_killMutant18(self):
        actual = Triangle.classify(10, 10, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test_killMutant20(self):
    #     actual = Triangle.classify((1 << 31) | 5, 10, (1 << 31) | 6)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test_killMutant59(self):
        pass  # EQUIVALENT

    def test_killMutant63(self):
        actual = Triangle.classify(3, 4, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant66(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant70(self):
        actual = Triangle.classify(4, 7, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant73(self):
        actual = Triangle.classify(1, 3, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test_killMutant76(self):
    #     actual = Triangle.classify((1 << 31) - 2, (1 << 30), (1 << 30) - 1)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test_killMutant80(self):
        actual = Triangle.classify(5, 7, 6)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_killMutant81(self):
        actual = Triangle.classify(7, 3, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant84(self):
        actual = Triangle.classify(3, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test_killMutant87(self):
    #     actual = Triangle.classify((1 << 30), (1 << 30) - 1, (1 << 31) - 2)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test_killMutant101(self):
        pass  # EQUIVALENT

    def test_killMutant105(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    # def test_killMutant111(self):
    #     a = (1 << 31) - 1
    #     b = (1 << 31) - 2
    #     c = (1 << 31) - 1
    #     actual = Triangle.classify(a, b, c)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test_killMutant122(self):
        actual = Triangle.classify(10, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant125(self):
        actual = Triangle.classify(10, 21, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test_killMutant128(self):
    #     a = (1 << 31) - 2
    #     b = (1 << 31) - 1
    #     c = (1 << 31) - 1
    #     actual = Triangle.classify(a, b, c)
    #     expected = Triangle.Type.INVALID
    #     self.assertEqual(actual, expected)

    def test_killMutant136(self):
        # EQUIVALENT
        pass

    def test_killMutant139(self):
        actual = Triangle.classify(20, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()