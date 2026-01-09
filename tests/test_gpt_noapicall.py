# Scott Barfuss - 4/10/25
# Unit testing chat_with_gpt() without an API call
from unittest.mock import patch, MagicMock
from src.gpt_client import chat_with_gpt

# This mocks an actual network call; no real API request
@patch("src.gpt_client.client.chat.completions.create")

def test_gpt_success(mock_create):
    # Mock the response from the API call
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="Mock GPT reply!"))]
    mock_create.return_value = mock_response

    # Call the function with test data
    result = chat_with_gpt("This is a test prompt, please respond.")

    # Assert that the mocked response is returned correctly
    assert result == "Mock GPT reply!"
    mock_create.assert_called_once()

# This tests a failure instead
@patch("src.gpt_client.client.chat.completions.create",
        side_effect=Exception("API call failed"))
def test_gpt_failure(mock_create):
    # Call the function with test data
    result = chat_with_gpt("Test prompt")

    # Assert that the function handles the exception correctly
    assert "An error occurred" in result