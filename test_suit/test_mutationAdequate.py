import unittest
from isTriangle import Triangle


class MutantAdequateTest(unittest.TestCase):

    def test_killMutant1_2_3_15_16_36_38_40(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
    
    def test_killMutant4_7_11_17_32_44_45(self):
        self.assertEqual(Triangle.classify(4, 4, 5), Triangle.Type.ISOSCELES)

    def test_killMutant5_12_18_33_47_48(self):
        self.assertEqual(Triangle.classify(3, 5, 3), Triangle.Type.ISOSCELES)
    
    def test_killMutant6_19_43_50_51(self):
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)
    
    def test_killMutant8_9_10_13_14_26_30_34_35_42(self):
        self.assertEqual(Triangle.classify(7, 7, 7), Triangle.Type.EQUILATERAL)

    def test_killmutant21_27_28(self):
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
    
    def test_killMutant29(self):
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)

    def test_killMutant31(self):
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, -1), Triangle.Type.INVALID)

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



    # # Addressing Mutant 32
    # def test_killMutant32(self):
    #     self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
    #     self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)
    #     self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)

    # def test_classify_with_one_side_zero(self):
        
        
    #     self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)

    # def test_classify_with_one_side_negative(self):
    #     self.assertEqual(Triangle.classify(-1, 1, 1), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(1, -1, 1), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(1, 1, -1), Triangle.Type.INVALID)




    # def test_classify_scalene_triangles(self):
        
    #     self.assertEqual(Triangle.classify(6, 8, 10), Triangle.Type.SCALENE)
    #     self.assertEqual(Triangle.classify(12, 15, 17), Triangle.Type.SCALENE)
    
    # def test_classify_equilateral_triangles(self):
        
    #     self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
    #     self.assertEqual(Triangle.classify(2**31, 2**31, 2**31), Triangle.Type.EQUILATERAL)
    
    # def test_classify_isosceles_triangles(self):
        
    #     self.assertEqual(Triangle.classify(2**31, 2**31 - 1, 2**31 - 1), Triangle.Type.ISOSCELES)
    #     self.assertEqual(Triangle.classify(2**31 - 1, 2**31 - 1, 2**31), Triangle.Type.ISOSCELES)
    
    # def test_classify_invalid_triangles(self):
    #     self.assertEqual(Triangle.classify(0, 3, 4), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(5, 0, 4), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(5, 3, 0), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(-2, 3, 4), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(5, -2, 4), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(5, 3, -2), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)
    #     # New test cases to kill the second mutant
    #     self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
    #     self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)



if __name__ == '__main__':
    unittest.main()