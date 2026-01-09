import pytest
from unittest.mock import patch
from src.query_manager import generate_summary

""" This module contains testing for the generate_summary function in query_manager.py """

@patch("src.query_manager.chat_with_gpt", return_value="Here is a summary of your character: Elf Wizard with a Sage background.")
def test_generate_summary(mock_chat_with_gpt, capsys):
    """Test the generate_summary function with mocked GPT response."""
    # Call the function with test inputs
    generate_summary("Elf", "Wizard", "Sage")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the expected summary is printed
    assert "Character Summary:" in captured.out
    assert "Here is a summary of your character: Elf Wizard with a Sage background." in captured.out

    # Assert that chat_with_gpt was called with the correct prompt
    mock_chat_with_gpt.assert_called_once_with(
        "Create a summary for a D&D character with the following details:\n"
        "Race: Elf\nClass: Wizard\nBackground: Sage\n"
        "Include a brief backstory and personality traits."
    )
