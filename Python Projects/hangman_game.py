# simple hangman game where a word is displayed as a series of underscores (eg _ _ _ _ _) and the user is 
# made to guess letters until the word is spelled. A maximum number of attempts will be given before the
# man is hanged.

import random

# creating a bank of potential words to choose from

words = ['socks', 'mug', 'zucchini', 'phone', 'dentist']

# shuffling around the list so a new word is presented each time the program is ran
random.shuffle(words)
# choosing a word, splitting into characters and sticking it in a list
answer = list(words[0])
# variable going to be used for displaying the underscores
display = []
display.extend(answer) # contains answers

# replacing the answer with underscores so the display to user is in the form _ _ _ _ 
for i in range(len(display)):
    display[i] = "_"

# putting the space between each underscore
print(' '.join(display))

# initializing the accumulator
attempts = 0

# game starts
while attempts <= len(display):

    # getting user's guess and accounting for them putting in upper case
    guess = input('Guess a letter: ')
    guess.lower()
    
    # if the character is not found, prints the amount of attempts left
    if guess not in answer:
        print(str(len(display) - attempts) + ' attempt(s) left.' )
        attempts += 1

    # iterating through the answer to see if the user's guess matches, and then replaces one of the underscores
    # with the correct letter if found
    for i in range(len(display)):
        if answer[i] == guess:
            display[i] = guess
            attempts += 1

    # prints the display
    print(' '.join(display))

    # if attempts run out, prints game over and exits
    if attempts > len(display):
        print('Game over! You lose!')
        exit
    