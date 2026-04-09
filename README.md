# D&D Character Creator

## Project Overview
This project is an AI-Powered D&D Character Creator. The goal was to develop backend code that interacts with the ChatGPT API, allowing users to create fantasy characters in an innovative AI-powered interface.

## Features
- Accepts user input and optimizes queries before sending them to ChatGPT.
- Enhances responses by providing structured instructions around user queries.
- Simulates a **Dungeons & Dragons (D&D) character creation** process using ChatGPT.
- Uses Quart for asynchronous handling of requests.
- Built with Python 3.13.2 and Poetry 1.8.3 for dependency management.

## Technologies Used
- **Python**: Version 3.13.2
- **Poetry**: Version 1.8.3 (for dependency and environment management)
- **Quart**: For handling API interactions
- **ChatGPT API**: To generate responses from optimized queries

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.13.2
- Poetry 1.8.3

### Setup
1. Clone the repository and navigate to the project directory:
   ```sh
   git clone <repo-url>
   cd Team2-Project
   ```
2. Install dependencies:
   ```sh
   poetry install
   ```
3. Activate the virtual environment:
   ```sh
   poetry shell
   ```

## Usage
Run the GPT Optimizer with:
```sh
python main.py
```

### D&D Character Creator
The program includes a **Dungeons & Dragons (D&D) character creation feature**. Follow the prompts to create a character by selecting a race, class, and background. ChatGPT will generate a summary of your character, including a backstory and personality traits.

## Interacting with ChatGPT API Using Python

### Prerequisites
1. **Install OpenAI's Python package**:
   ```bash
   pip install openai
   ```
2. **Obtain an API Key**:
   - Sign up at [OpenAI](https://platform.openai.com/) and generate an API key.

### Simple Python Script
```python
import openai

# Set your API key
openai.api_key = "your-api-key-here"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" for a cheaper/faster option
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,  # Adjust creativity level (0.0 = strict, 1.0 = very random)
    )
    return response["choices"][0]["message"]["content"]

# Example usage
user_input = input("You: ")
reply = chat_with_gpt(user_input)
print("ChatGPT:", reply)
```

### How It Works
1. **Imports `openai`** – The OpenAI library is used to make API calls.
2. **Sets the API key** – Replace `"your-api-key-here"` with your actual API key.
3. **Defines `chat_with_gpt(prompt)`** – Sends a message to ChatGPT and retrieves a response.
4. **Runs an example** – Takes user input, sends it to ChatGPT, and prints the response.

## Enhancements
Future improvements could include:
- Adding **error handling** for API calls.
- Supporting **conversation history** for more context-aware responses.
- Expanding the D&D character creation feature with additional customization options.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Authors
- Jordan Waite
- Benesh Shah
- Collin Kress
- Scott Barfuss
- Danni Hampton
