# %%
import random 
word_list = ["mango", "papaya", "grapes", "guava", "banana"]
word = random.choice(word_list) 
print(word)
#%%
guess = input("Enter a alphabetical letter :").lower()

if len(guess) == 1 and guess.isalpha() == True and guess.isdigit() == False:
    print("Good Guess!")
else:
    print("Oops!This is not a valid input.Please enter only one alphabetical letter.")

# %%
