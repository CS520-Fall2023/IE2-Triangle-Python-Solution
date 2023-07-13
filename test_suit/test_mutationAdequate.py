import unittest
from isTriangle import Triangle


class MutantAdequateTest(unittest.TestCase):

    def test_killMutant1(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    #new    
    def test_killMutant2(self):
        actual = Triangle.classify(3, 3, 3)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    #new  
    def test_killMutant3(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)


    def test_killMutant4(self):
        actual = Triangle.classify(-1, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new  
    def test_killMutant5(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new  
    def test_killMutant6(self):
        actual = Triangle.classify(10, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new  
    def test_killMutant7(self):
        actual = Triangle.classify(20, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new
    def test_killMutant8(self):
        actual = Triangle.classify(1, 3, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant9(self):
        actual = Triangle.classify(10, -1, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new
    def test_killMutant10(self):
        actual = Triangle.classify(3, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant11(self):
        actual = Triangle.classify(pow(2, 31)^-5, pow(2, 31)^-6, 10)
        expected = Triangle.Type.INVALID
        print(actual, expected)
        self.assertEqual(actual, expected)
    #new
    def test_killMutant12(self):
        actual = Triangle.classify(2**31, 2**31, 2**31)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    #new
    def test_killMutant13(self):
        actual = Triangle.classify(3, 4, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    #new
    def test_killMutant14(self):
        actual = Triangle.classify(7, 3, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


    def test_killMutant18(self):
        actual = Triangle.classify(10, 10, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant20(self):
        actual = Triangle.classify(pow(2, 31)^-5, 10, pow(2, 31)^-6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

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

    def test_killMutant76(self):
        actual = Triangle.classify(pow(2, 31)^-2, pow(2, 30), pow(2, 31)^-1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

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

    def test_killMutant87(self):
        actual = Triangle.classify(pow(2, 30), pow(2, 30)^-1, pow(2, 31)^-2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant101(self):
        pass  # EQUIVALENT

    def test_killMutant105(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_killMutant111(self):
        a = 1 << 31 - 1
        b = 1 << 31 - 1
        c = 1 << 31
        actual = Triangle.classify(a, b, c)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant122(self):
        actual = Triangle.classify(10, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant125(self):
        actual = Triangle.classify(10, 21, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant128(self):
        a = 1 << 31 
        b = 1 << 31 - 1
        c = 1 << 31 - 1
        actual = Triangle.classify(a, b, c)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant136(self):
        # EQUIVALENT
        pass

    def test_killMutant139(self):
        actual = Triangle.classify(20, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    #new
    def test_classify_invalid_triangles(self):
        self.assertEqual(Triangle.classify(0, 3, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 0, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 3, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-2, 3, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, -2, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 3, -2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)

        # # Test cases with large values using pow() function
        # self.assertEqual(Triangle.classify(pow(2, 31) - 1, pow(2, 31) - 1, pow(2, 31) - 1), Triangle.Type.INVALID)
        # self.assertEqual(Triangle.classify(pow(2, 31), pow(2, 31), pow(2, 31) - 1), Triangle.Type.INVALID)
        # self.assertEqual(Triangle.classify(pow(2, 31) - 1, pow(2, 31), pow(2, 31)), Triangle.Type.INVALID)
    #new
    def test_classify_scalene_triangles(self):
        self.assertEqual(Triangle.classify(5, 7, 9), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(8, 6, 10), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
    #new
    def test_classify_equilateral_triangles(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)
    #new
    def test_classify_isosceles_triangles(self):
        self.assertEqual(Triangle.classify(4, 4, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 5, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)
    #new
    def test_classify_additional_triangles(self):
        # Additional test cases to increase code coverage
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(6, 8, 10), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(12, 15, 17), Triangle.Type.SCALENE)

        self.assertEqual(Triangle.classify(7, 7, 7), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)

        self.assertEqual(Triangle.classify(4, 4, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 5, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)

        self.assertEqual(Triangle.classify(2**31, 2**31, 2**31), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(2**31, 2**31 - 1, 2**31 - 1), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2**31 - 1, 2**31 - 1, 2**31), Triangle.Type.ISOSCELES)




if __name__ == '__main__':
    unittest.main()