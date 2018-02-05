from returning_strings import *
import unittest

class MyTest(unittest.TestCase):
    def test_ryan(self):
        self.assertEquals(greet('Ryan'), "Hello, Ryan how are you doing today?")

if __name__ == '__main__':
    unittest.main()
