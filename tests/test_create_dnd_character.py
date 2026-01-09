import pytest
from unittest.mock import patch
from src.query_manager import create_dnd_character

""" This module contains testing for the create_dnd_character function in query_manager.py """

@patch("builtins.input", side_effect=["Elf", "Wizard", "Sage", "extra_input", "exit"])  # Added more inputs
@patch("src.query_manager.chat_with_gpt", side_effect=[
    "Human, Elf, Dwarf, Halfling",  # Mock response for race
    "Fighter, Wizard, Rogue, Cleric",  # Mock response for class
    "Noble, Soldier, Criminal, Sage",  # Mock response for background
    "Here is a summary of your character: Elf Wizard with a Sage background."  # Mock response for summary
])
def test_create_dnd_character(mock_chat_with_gpt, mock_input, capsys):
    """Test the create_dnd_character function with mocked inputs and GPT responses."""
    create_dnd_character()

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the expected prompts and outputs are printed
    assert "Welcome to the D&D Character Creator!" in captured.out
    assert "Type 'exit', 'quit', or 'end' at any time to stop." in captured.out
    assert "Available Races:" in captured.out
    assert "Available Classes:" in captured.out
    assert "Available Backgrounds:" in captured.out
    assert "Character Summary:" in captured.out
    assert "Character creation complete! Enjoy your adventure!" in captured.out

    # Assert that chat_with_gpt was called with the correct prompts
    assert mock_chat_with_gpt.call_count == 4  # Ensure all four calls were made
    assert "Help the user choose a race" in mock_chat_with_gpt.call_args_list[0][0][0]
    assert "Now help them choose a class" in mock_chat_with_gpt.call_args_list[1][0][0]
    assert "Now help them choose a background" in mock_chat_with_gpt.call_args_list[2][0][0]
    assert "Create a summary for a D&D character" in mock_chat_with_gpt.call_args_list[3][0][0]

@patch("builtins.input", side_effect=["exit"])  # User exits at race selection
@patch("src.query_manager.chat_with_gpt", return_value="Human, Elf, Dwarf, Halfling")
def test_exit_at_race_selection(mock_chat_with_gpt, mock_input, capsys):
    """Test exiting character creation at the race selection stage."""
    create_dnd_character()
    captured = capsys.readouterr()
    assert "Exiting character creation. Goodbye!" in captured.out
    assert mock_chat_with_gpt.call_count == 1  # GPT is called once for race

@patch("builtins.input", side_effect=["Elf", "quit"])  # User exits at class selection
@patch("src.query_manager.chat_with_gpt", side_effect=[
    "Human, Elf, Dwarf, Halfling",  # Mock response for race
    "Fighter, Wizard, Rogue, Cleric"  # Mock response for class
])
def test_exit_at_class_selection(mock_chat_with_gpt, mock_input, capsys):
    """Test exiting character creation at the class selection stage."""
    create_dnd_character()
    captured = capsys.readouterr()
    assert "Exiting character creation. Goodbye!" in captured.out
    assert mock_chat_with_gpt.call_count == 2  # GPT is called for race and class

@patch("builtins.input", side_effect=["Elf", "Wizard", "end"])  # User exits at background selection
@patch("src.query_manager.chat_with_gpt", side_effect=[
    "Human, Elf, Dwarf, Halfling",  # Mock response for race
    "Fighter, Wizard, Rogue, Cleric",  # Mock response for class
    "Noble, Soldier, Criminal, Sage"  # Mock response for background
])
def test_exit_at_background_selection(mock_chat_with_gpt, mock_input, capsys):
    """Test exiting character creation at the background selection stage."""
    create_dnd_character()
    captured = capsys.readouterr()
    assert "Exiting character creation. Goodbye!" in captured.out
    assert mock_chat_with_gpt.call_count == 3  # GPT is called for race, class, and background
