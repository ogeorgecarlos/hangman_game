import os
import random
import sys
from time import sleep
from hangman_wordbank import HANGMANPICS, words


# this function create a pattern 
# for the headers in the game
def header(text):
    print()
    print(40*'-')
    print(f'{text:^40}')
    print(40*'-')


# Variables used in the program
letter_chosen = ''
error_counter = 0
right_letters = set()
hangman_length = len(HANGMANPICS)

# ---> MAIN PROGRAM < ---
header("Step one!")

# Input and verifyer of user's name
while True:
    user_name = input("✅ Hey! What's your nickname?\n").strip().capitalize()
    if user_name == '':
        print('❌ Please, enter with a nickname.\n')
    else:
        break


header(f"Let's start, {user_name}!")
chosen_word = random.choice(words)

# This 'for' will print the progress
while True:
    # ....
    if len(right_letters) == len(chosen_word):
        header('✌ You Win!!')
        print(f"😎 You find the secret word: '{chosen_word.upper()}'!!")
        sleep(2)
        print()
        sys.exit()

    # ....
    print('\n🤐 Chooose a letter and find the secret word\n')
    for letter in chosen_word:
        if letter in right_letters:
            print(letter, end='')
        else:
            print(' _', end='')

    # This loop will validate the input (Jus letters, and just one letter)
    while True:
        letter_chosen = input("\n\n✅ Enter with a letter: ").strip().lower()
        if letter_chosen.isalpha() and len(letter_chosen) == 1:
            break
        else:
            print('❌ \nEnter with just one letter.')

    # This condition checks if it was a wrong choice
    # and print the hangman progress
    if letter_chosen not in chosen_word:
        error_counter += 1
        os.system('cls')
        header('😥 Oh! You missed... ')
        sleep(0.5)
        print(HANGMANPICS[error_counter-1])
        sleep(1)
    else:
        right_letters.add(letter_chosen)

    # If the hangman's pic is completed the game is over
    if error_counter == hangman_length:
        header('😥 You loose')
        print(f'🤣 The secret word was {chosen_word.upper()}')
        sleep(2)
        print()
        sys.exit()

    header('✌ One more chance!')
