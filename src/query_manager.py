from src.gpt_client import chat_with_gpt

def choose_race():
    """Handles race selection with GPT assistance."""
    race_prompt = (
        "You are a D&D assistant. Help the user choose a race for their character. "
        "Provide a brief description of popular races like Human, Elf, Dwarf, Halfling, etc."
    )
    race_response = chat_with_gpt(race_prompt)
    print("\nAvailable Races:\n", race_response)
    race = input("Choose a race: ")
    return race

def choose_class(race):
    """Handles class selection based on chosen race."""
    class_prompt = (
        f"The user has chosen the race '{race}'. Now help them choose a class. "
        "Provide a brief description of popular classes like Fighter, Wizard, Rogue, Cleric, etc."
    )
    class_response = chat_with_gpt(class_prompt)
    print("\nAvailable Classes:\n", class_response)
    char_class = input("Choose a class: ")
    return char_class

def choose_background(race, char_class):
    """Handles background selection based on chosen race and class."""
    background_prompt = (
        f"The user has chosen the race '{race}' and the class '{char_class}'. "
        "Now help them choose a background. Provide a brief description of popular backgrounds like "
        "Noble, Soldier, Criminal, Sage, etc."
    )
    background_response = chat_with_gpt(background_prompt)
    print("\nAvailable Backgrounds:\n", background_response)
    background = input("Choose a background: ")
    return background

def generate_summary(race, char_class, background):
    """Generates a character summary based on chosen details."""
    summary_prompt = (
        f"Create a summary for a D&D character with the following details:\n"
        f"Race: {race}\nClass: {char_class}\nBackground: {background}\n"
        "Include a brief backstory and personality traits."
    )
    summary_response = chat_with_gpt(summary_prompt)
    print("\nCharacter Summary:\n", summary_response)

def create_dnd_character():
    """Manages the character creation flow."""
    print("Welcome to the D&D Character Creator!")
    print("Type 'exit', 'quit', or 'end' at any time to stop.\n")

    race = choose_race()
    if race.lower() in ["exit", "quit", "end"]:
        print("Exiting character creation. Goodbye!")
        return

    char_class = choose_class(race)
    if char_class.lower() in ["exit", "quit", "end"]:
        print("Exiting character creation. Goodbye!")
        return

    background = choose_background(race, char_class)
    if background.lower() in ["exit", "quit", "end"]:
        print("Exiting character creation. Goodbye!")
        return

    generate_summary(race, char_class, background)
    print("\nCharacter creation complete! Enjoy your adventure!")

if __name__ == "__main__":
    create_dnd_character()
