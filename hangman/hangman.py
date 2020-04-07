import os
import random

# Defining a list with the words to guess
WORDS = [
    'Monkey',
    'Laptop',
    'Notebook',
    'Monitor',
    'Television',
    'Superman',
    'Pokemon',
]
name = None

def run_game():
    # Initial values for the game
    word = random.choice(WORDS)
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while turns > 0:
        placeholder = ''
        missed = 0

        # Loop that checks if a guess is right or not
        for letter in word.lower():
            # if the letter is in the word to guess added it to the placeholder for the word
            # otherwise, add a _ as a missing letter
            if letter.lower() in guessmade:
                placeholder = placeholder + letter
            else:
                placeholder = placeholder + '_'
        
        # if the placeholder finally matches the word to guess
        # we finish the game
        if placeholder == word.lower():
            print(f"You guessed the word {placeholder}")
            print('You win!')
            break

        print(f"{turns} turns left.")
        print(placeholder)
        guess_input = input("Enter your guess: ")

        # if the input letter by the user is a valid letter add it to the guessmade
        # otherwise, tell the user to enter a right word
        if guess_input.lower() in valid_letters:
            guessmade = guessmade + guess_input
        else:
            print("Enter a valid charanter. [A-Z]")
            guess_input = input("Enter your guess: ")
        
        # if the guess input is not any letter in the word to guess
        # decrease the turns count
        if guess_input not in word:
            turns = turns - 1
            
            # if guess count = 0 show message
            if turns == 0:
                print(f"The word to guess was {word.title()}")
                print("Better luck next time.\n")


def init_ui(name):
    print(f"Welcome to the Hangman Game, {name.title()}.")
    print("-----------------------------------------------")
    print("Try to guess the word in less than 10 attempts.")


# 
name = input("Enter your name: ")
while True:
    os.system("clear")
    init_ui(name)
    run_game()
    if input("Do you wanna try again? Y/N: ").lower() == 'n':
        break

