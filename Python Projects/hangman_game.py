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

for i in range(len(display)):
    display[i] = "_"

print(' '.join(display))

attempts = 0

while attempts < len(display):

    for i in range(display):
