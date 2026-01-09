import pytest
from src.query_manager import choose_race


def test_choose_race(mocker, capsys):
    """Test choose_race with valid input"""
    gpt_mock_reply = "1. Human\n2. Elf\n3. Dwarf\n4. Halfling"
    mock_chat_with_gpt = mocker.patch(
        "src.query_manager.chat_with_gpt",
        return_value = gpt_mock_reply
    )
    mock_input = mocker.patch("builtins.input", return_value="User Input")

    result = choose_race()

    # capture the output
    captured_output = capsys.readouterr()

    mock_chat_with_gpt.assert_called_once()
    assert captured_output.out == "\nAvailable Races:\n " + gpt_mock_reply + "\n"

    mock_input.assert_called_once_with("Choose a race: ")
    assert result == "User Input"
