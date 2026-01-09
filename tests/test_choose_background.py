import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.query_manager import choose_background

class TestChooseBackground(unittest.TestCase):

    @patch('builtins.input', side_effect=['Criminal'])
    @patch('src.query_manager.chat_with_gpt')  # Mock GPT call
    def test_valid_background_input(self, mock_gpt, mock_input):
        mock_gpt.return_value = "Popular backgrounds: Noble, Criminal, Sage, Soldier"
        result = choose_background("Elf", "Wizard")
        self.assertEqual(result, "Criminal")

    @patch('builtins.input', side_effect=['Folk Hero'])
    @patch('src.query_manager.chat_with_gpt')
    def test_custom_background_input(self, mock_gpt, mock_input):
        mock_gpt.return_value = "Some backgrounds include Acolyte, Folk Hero, and Noble."
        result = choose_background("Human", "Cleric")
        self.assertEqual(result, "Folk Hero")

if __name__ == '__main__':
    unittest.main()

