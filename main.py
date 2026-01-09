import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.query_manager import create_dnd_character

if __name__ == "__main__":
    print("Starting the D&D Character Creator...")
    create_dnd_character()