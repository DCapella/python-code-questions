from single_digit import *
import unittest

class MyTest(unittest.TestCase):
    def test_single_digit(self):
        self.assertEquals(single_digit(5665), 5)

    def test_single_digit_two(self):
        self.assertEquals(single_digit(123456789), 1)

    def test_single_digit_single_number(self):
        self.assertEquals(single_digit(5), 5)

if __name__ == '__main__':
    unittest.main()
