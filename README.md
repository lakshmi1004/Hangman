# Hangman

    Project Title: HAngman
## Table of Contents
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions
Usage instructions
File structure of the project
License information
    
## How to Use

    Ensure you have Python installed on your system.
    Copy the provided code into a Python script.
    Run the script, and the game will start.
    Follow the prompts to guess letters of the secret word.
## A description of the project:
    
    Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

##  Aim of the project:
    Create this Hangman project in OOPS
    
## what it does:
    1.Set Up the Game Structure: Create the basic structure of the game, including initializing variables such as the word to be guessed, the number of allowed guesses, and the guessed letters.

    2.Display Initial Interface: Print out the initial interface of the game, which could be a series of underscores representing each letter in the word to be guessed, along with any relevant information like remaining guesses.

    3.Implement Guessing Logic: Allow the player to input guesses. Validate the input to ensure it's a single letter. Check if the guessed letter is in the word and update the interface accordingly.

    4.Update Game State: Keep track of the state of the game, including the guessed letters, remaining guesses, and the current state of the word being guessed.

    5.Handle Win/Loss Conditions: Check if the player has guessed all the letters in the word or if they have run out of guesses. If so, end the game and display an appropriate message.

    6.Add Hangman Art: Optionally, you can include ASCII art for the hangman that updates with each incorrect guess to make the game more visually appealing.

    7.Provide Replay Option: After the game ends, ask the player if they want to play again. If yes, reset the game and start over.
    
## Lessons Learned
In the process of developing the Hangman Game, the following key lessons are:
- Object-oriented programming (OOP) concepts such as classes, objects, methods, and attributes.
- How to handle user input and validate it to ensure the program operates correctly.
- String manipulation techniques for comparing strings, extracting substrings, and formatting output.
- Algorithmic problem-solving skills, particularly in determining the game logic and implementing the win/lose conditions.
- How to structure a Python project, organize code into modules and functions, and manage dependencies.

- Git Hub - local - remote synchronization
    
        
## Installation
To run the Hangman game, follow these steps:
1. Clone this repository to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. Navigate to the project directory in your terminal.
4. Run the command `python hangman.py` to start the game.
    
## Usage
Once the game is running, follow the prompts to guess letters and try to uncover the secret word. You have a limited number of lives, so be careful with your guesses!

## File Structure
The project directory contains the following files:
- `milestone_4.py`: The main Python script containing the Hangman game implementation.
- `README.md`: This file, providing information about the project.
- `LICENSE`: License information for the project.
## License
This project is licensed under the [MIT License](LICENSE).
