
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def choose_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess, secretword, word_guessed):
        guess = guess.lower()
        if guess in secretword:
            print("Good guess! '{}' is in the word".format(guess))
            for i in range(len(secretword)):
                if secretword[i] == guess:
                    word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print("Sorry, '{}' is not in the word. Try again.".format(guess))
        return word_guessed

    def ask_for_input(self):
        while True:
            guess = input("Enter an alphabetical letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already guessed '{}'. Try again.".format(guess))
                else:
                    self.list_of_guesses.append(guess)
                    return guess
            else:
                print("Oops! This is not a valid input. Please enter only one alphabetical letter.")

    def play_game(self):
        word = self.choose_word()
        secret = list(word)
        word_guessed = ["_" for _ in secret]
        print(word_guessed)  # For testing purposes, remove in final version
        self.num_letters = len(secret)
        while self.num_lives > 0 and self.num_letters > 0:
            guess = self.ask_for_input()
            word_guessed = self.check_guess(guess, secret, word_guessed)
            print("Word guessed so far:", " ".join(word_guessed))
            if self.num_letters == 0:
                print("Congratulations! You've guessed the word '{}' correctly!".format(word))
            elif guess not in secret:
                self.num_lives -= 1
                print("Lives left:", self.num_lives)
        else:
            if self.num_lives == 0:
                print("Sorry, you've run out of lives. The word was '{}'.".format(word))

if __name__ == "__main__":
    word_list = ["mango", "papaya", "grapes", "guava", "banana", 'Rambutan', "Chickoo"]
    game = Hangman(word_list)
    game.play_game()
