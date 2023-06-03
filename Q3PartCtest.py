import unittest
from unittest.mock import patch
from io import StringIO
from Q3PartC import guessing_game

class GuessingGameTestCase(unittest.TestCase):
    def test_guessing_low_number(self):
        with patch('builtins.input', side_effect=['30', '42']):
            with patch('sys.stdout', new=StringIO()) as output:
                guessing_game()
                self.assertEqual(output.getvalue().strip(), "Too low\nYou got it!")

    def test_guessing_high_number(self):
        with patch('builtins.input', side_effect=['70', '42']):
            with patch('sys.stdout', new=StringIO()) as output:
                guessing_game()
                self.assertEqual(output.getvalue().strip(), "Too high\nYou got it!")

    def test_guessing_correct_number_first_attempt(self):
        with patch('builtins.input', return_value='42'):
            with patch('sys.stdout', new=StringIO()) as output:
                guessing_game()
                self.assertEqual(output.getvalue().strip(), "You got it!")

    def test_guessing_correct_number_multiple_attempts(self):
        with patch('builtins.input', side_effect=['30', '60', '42']):
            with patch('sys.stdout', new=StringIO()) as output:
                guessing_game()
                self.assertEqual(output.getvalue().strip(), "Too low\nToo high\nYou got it!")

if __name__ == '__main__':
    unittest.main()
