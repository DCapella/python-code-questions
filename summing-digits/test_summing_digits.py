from summing_digits import *
import unittest

class MyTest(unittest.TestCase):
    def testA(self):
        test = sum_digits(10)
        result = 1
        self.assertEqual(test, result)

    def testB(self):
        test = sum_digits(99)
        result = 18
        self.assertEqual(test, result)

    def testC(self):
        test = sum_digits(-32)
        result = 5
        self.assertEqual(test, result)

if __name__ == '__main__':
    unittest.main()
