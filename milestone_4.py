import random 

def wordlist():
    # Wordlist created. To get random words from the list random.choice method() is called.
    word_list = ["mango", "papaya", "grapes", "guava", "banana"]
    word = random.choice(word_list) 
    return word

def secretword(word):    
    secretword = list(word)
    print(secretword)
    return secretwordgit 

def check_guess(guess, secretword):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secretword:
        print("Good guess! '{}' is in the word".format(guess))
    else:
        print("Sorry, '{}' is not in the word. Try again.".format(guess))

def ask_for_input():
    
    # Step 2: Prompt the user to enter a single alphabetical letter
    guess = input("Enter an alphabetical letter: ").lower()
    # Step 3: Check if the input is a valid guess
    if len(guess) == 1 and guess.isalpha() and not guess.isdigit():
        return guess
    # Step 3: Check if the input is a valid guess
    else:
        print("Oops! This is not a valid input. Please enter only one alphabetical letter.")
        return None
    
# Main function to execute the game
def main():
    word = wordlist()
    secret = secretword(word)
    while True:
        guess = ask_for_input()
        if guess is not None:
            check_guess(guess, secret)
            if set(secret) == set(guess):
                print("Congratulations! You've guessed the word '{}' correctly!".format(word))
            break

if __name__ == "__main__":
    main()




# %%
