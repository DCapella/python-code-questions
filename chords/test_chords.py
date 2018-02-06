from chords import *
import unittest

class MyTest(unittest.TestCase):
    def test_one(self):
        test = chords("C")
        result = [["C", "E", "G"], ["C", "D#", "G"]]
        self.assertEquals(test, result)

    def test_two(self):
        test = chords("F")
        result = [["F", "A", "C"], ["F", "G#", "C"]]
        self.assertEquals(test, result)

    def test_three(self):
        test = chords("G")
        result = [["G", "B", "D"], ["G", "A#", "D"]]
        self.assertEquals(test, result)

if __name__ == '__main__':
    unittest.main()
