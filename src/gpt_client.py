import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Access API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    """Interact with GPT using the Chat Completions API."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use the appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while communicating with GPT: {e}"

# Example usage/ running this file directly
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        reply = chat_with_gpt(user_input)
        print("ChatGPT:", reply)
