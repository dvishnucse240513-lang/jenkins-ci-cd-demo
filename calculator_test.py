
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtraction(self):
        self.assertEqual(subtract(20, 10), 10)

if __name__ == '__main__':
    unittest.main()
