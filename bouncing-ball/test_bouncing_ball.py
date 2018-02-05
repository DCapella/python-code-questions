from bouncing_ball import *
import unittest

class MyTest(unittest.TestCase):
    def test_one(self):
        test = bouncing_ball(2, 0.5)
        result = 1
        self.assertEquals(test, result)

    def test_two(self):
        test = bouncing_ball(4, 0.5)
        result = 2
        self.assertEquals(test, result)

    def test_three(self):
        test = bouncing_ball(10, 0.1)
        result = 1
        self.assertEquals(test, result)

    def test_four(self):
        test = bouncing_ball(100, 0.1)
        result = 2
        self.assertEquals(test, result)

    def test_five(self):
        test = bouncing_ball(9, 0.3)
        result = 2
        self.assertEquals(test, result)

    def test_six(self):
        test = bouncing_ball(30, 0.3)
        result = 3
        self.assertEquals(test, result)

if __name__ == '__main__':
    unittest.main()
