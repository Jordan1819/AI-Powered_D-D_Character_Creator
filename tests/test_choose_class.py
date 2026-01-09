import pytest
from unittest.mock import patch
from src.query_manager import choose_class


def test_choose_class():
    fake_race = "Elf"
    fake_gpt_response = "Fighter, Wizard, Rogue, Cleric"
    fake_input = "Wizard"

    with patch("src.query_manager.chat_with_gpt", return_value=fake_gpt_response):
        with patch("builtins.input", return_value=fake_input):
            result = choose_class(fake_race)

    assert result == fake_input