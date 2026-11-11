
import unittest
from calculator import add, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(15, 25), 40)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_negative(self):
        self.assertEqual(add(-5, 10), 5)

if __name__ == "__main__":
    unittest.main()
