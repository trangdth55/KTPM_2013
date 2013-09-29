'''
Created on 23-09-2013

@author: Chun Trang
'''
import unittest
import math
from decimal import Decimal
from __init__ import detect_triangle


class Test(unittest.TestCase):

    def testName1(self):
        self.assertAlmostEqual(detect_triangle(-1,2,3), "Loi bien dau vao")
    def testName2(self):
        self.assertAlmostEqual(detect_triangle(1,-2,3), "Loi bien dau vao")
    def testName3(self):
        self.assertAlmostEqual(detect_triangle(1,2,-3), "Loi bien dau vao")
    def testName4(self):
        self.assertAlmostEqual(detect_triangle(3,1,(2**32+3)), "Loi bien dau vao")
    def testName5(self):
        self.assertAlmostEqual(detect_triangle((2**32+5),1,3), "Loi bien dau vao")
    def testName6(self):
        self.assertAlmostEqual(detect_triangle(1,(2**32),3), "Loi bien dau vao")
    def testName7(self):
        self.assertAlmostEqual(detect_triangle(5,'b',9.0), "Loi bien dau vao")
    def testName8(self):
        self.assertAlmostEqual(detect_triangle(2,4.5,'c'), "Loi bien dau vao")    
    def testName9(self):
        self.assertAlmostEqual(detect_triangle("D",2,3.1), "Loi bien dau vao")
    def testName10(self):
        self.assertAlmostEqual(detect_triangle(3,3.0,3.0), "Tam giac deu")
    def testName11(self):
        self.assertAlmostEqual(detect_triangle(1,1,math.sqrt(2)), "Tam giac vuong can")
    def testName12(self):
        self.assertAlmostEqual(detect_triangle(2,math.sqrt(8),2), "Tam giac vuong can")
    def testName13(self):
        self.assertAlmostEqual(detect_triangle(math.sqrt(162),9.0,9), "Tam giac vuong can")
    def testName14(self):
        self.assertAlmostEqual(detect_triangle(3.0,3,5), "Tam giac can")
    def testName15(self):
        self.assertAlmostEqual(detect_triangle(15.0,7,15), "Tam giac can")
    def testName16(self):
        self.assertAlmostEqual(detect_triangle(10**-9,2**32-1,2**32-1), "Tam giac can")
    def testName17(self):
        self.assertAlmostEqual(detect_triangle(3,4,5.0), "Tam giac vuong")
    def testName18(self):
        self.assertAlmostEqual(detect_triangle(12.0,13,5), "Tam giac vuong")
    def testName19(self):
        self.assertAlmostEqual(detect_triangle(4,math.sqrt(48),8.0), "Tam giac vuong")
    def testName20(self):
        self.assertAlmostEqual(detect_triangle(3,2.0,4.98), "Tam giac thuong")
    def testName21(self):
        self.assertAlmostEqual(detect_triangle(0,1,2.2), "Khong phai la tam giac")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testcheck']
    unittest.main()
