"""
    part of the code wars solutions repository

"""
# counts vowels in a given string

def get_count(input_str):
    num_vowels = 0
    for ch in input_str:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            num_vowels+=1   
    return num_vowels

import math     # math library

# 0.5 litres drank per hour, returns total litres consumed, always rounded down. 

def litres(time):
    return math.floor(time*0.5)

