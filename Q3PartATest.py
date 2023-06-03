import unittest
from Q3PartA import percentage

class PercentageTestCase(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(percentage(5, 10), 50)  # Test Case 1

    def test_invalid_input_1(self):
        self.assertEqual(percentage(0, 10), -1)  # Test Case 2

    def test_invalid_input_2(self):
        self.assertEqual(percentage(5, 5), -1)  # Test Case 3

    def test_invalid_input_3(self):
        self.assertEqual(percentage(-5, 10), -1)  # Test Case 4

    def test_invalid_input_4(self):
        self.assertEqual(percentage(10, -5), -1)  # Test Case 5

if __name__ == '__main__':
    unittest.main()
