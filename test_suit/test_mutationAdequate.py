import unittest
from isTriangle import Triangle


class MutantAdequateTest(unittest.TestCase):

    def test_killMutant1_2_3_15_16_36_38_40(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def test_killMutant4_7_11_17_32_44_45(self):
        actual = Triangle.classify(4, 4, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_killMutant5_12_18_33_47_48(self):
        actual = Triangle.classify(3, 5, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_killMutant6_19_43_50_51(self):
        actual = Triangle.classify(5, 4, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test_killMutant8_9_10_13_14_26_30_34_35_42(self):
        actual = Triangle.classify(7, 7, 7)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_killmutant21_27_28(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_killMutant29(self):
        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant31a(self):
        actual = Triangle.classify(1, 1, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant31b(self):
        actual = Triangle.classify(1, 1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant52(self):
        actual = Triangle.classify(20, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    #new
    def test_killMutant22_41(self):
        actual = Triangle.classify(3, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


    # #new
    def test_killMutant37(self):
        actual = Triangle.classify(3, 4, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


    def test_killMutant39(self):
        actual = Triangle.classify(4, 7, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_killMutant23_24_25_46(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)     

    def test_killMutant49(self):
        actual = Triangle.classify(10, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
