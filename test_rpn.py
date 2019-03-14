import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_exponent(self):
        result = rpn.calculate("10 2 ^")
        self.assertEqual(1024, result)

#TestBasics tb;

