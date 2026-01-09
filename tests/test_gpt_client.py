from unittest.mock import MagicMock, patch
import pytest

def test_openai_response_mock():
    mock_response = MagicMock()
    mock_response.output_text = "To check if an object is an instance of a class, use isinstance()"

    with patch("openai.OpenAI") as MockClient:
        # Mock the client and its method chain
        mock_client = MockClient.return_value
        mock_client.responses.create.return_value = mock_response

        # Call the function (or test code block) using the mock client
        client = MockClient(api_key="fake-api-key")
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a coding assistant that talks like a pirate.",
            input="How do I check if a Python object is an instance of a class?",
        )

        # Basic assertions
        output = response.output_text
        assert "instance" in output.lower() or "class" in output.lower()
        print(output)
