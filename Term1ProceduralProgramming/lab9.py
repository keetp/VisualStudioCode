# importing libraries
import random


# 1. Course Information. Dictionaries contain room number, instructors and meeting times relating to a course number.
# User enters a course number and the program returns the room number, instructor and time of the course.

def main():
    # course number/room number dictionary
    room_number_dct = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    # course number/instructor dictionary
    instructor_dct = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    # course number/meeting time dictionary
    meeting_time_dct = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.',
                        'CM241': '1:00 p.m.'}

    # user input for course number
    user_course = input('Please enter your course number to see your room, instructor and time slot: ').upper()

    # if course number is valid, determine where the values in the dictionary are and print them to the user.
    if user_course in room_number_dct:
        room_number = room_number_dct[user_course]
        instructor = instructor_dct[user_course]
        meeting_time = meeting_time_dct[user_course]

        print('Room number: ', room_number)
        print('Instructor: ', instructor)
        print('Time slot: ', meeting_time)
    else:
        # error message
        print('Course number not found.')


main()


#######################################################################################################################
# 2. Capital Quiz.

def main():
    # us states and capitals dictionary
    capital_dic = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhoda Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'}

    # making a list of state names
    states = list(capital_dic.keys())
    # accumulator for the amount of guesses
    guesses = 0
    # to keep the guessing game going
    more_attempts = True

    # choosing a random state
    state = random.choice(states)
    # setting its capital to a variable
    capital = capital_dic[state].lower()
    # asking for the user answer
    user_guess = input('What is the capital of ' + state + '? ').lower()

    while more_attempts is True:
        # if the input matches the capital, prints a congrats with the amount of guesses and ends the game
        if user_guess == capital:
            print('Correct! It took you', guesses, 'guesses.')
            more_attempts = False
        else:
            # if input doesn't match the capital, user is given another chance and the guesses variable increases by 1
            print('Nope! Try again. ')
            user_guess = input('What is the capital of ' + state + '? ').lower()
            guesses += 1
            more_attempts = True


main()


#######################################################################################################################

# 3. File Encryption/Decryption

# encryption program

def main():
    cryptogram_key_dct = {'a': '%', 'c': '!', 'b': 'T', 'e': '*', 'd': '3', 'g': '@', 'f': '#', 'i': 'r', 'h': 'G',
                          'k': '&',
                          'j': 'y', 'm': '6', 'l': 'V', 'o': 'U', 'n': 'E', 'q': 'I', 'p': 'A', 's': 'M', 'r': '^',
                          'u': 'Q',
                          't': '-', 'w': '_', 'v': '=', 'y': '+', 'x': 'F', 'z': '~'}
    user_file = input('What is the name of the file you are looking to encrypt?')
    infile = open(user_file, 'r')
    encrypted_file = open('encrypted.txt', 'w')

    for line in infile:
        for ch in line:
            if ch not in cryptogram_key_dct:
                encrypted_file.write(ch)
            else:
                encrypted_ch = cryptogram_key_dct[ch]
                encrypted_file.write(encrypted_ch)

    infile.close()
    encrypted_file.close()


main()


# decryption program. doesn't work perfectly due to not having enough unique symbols on my keyboard to correspond
# to each letter of the alphabet. Inevitable that the decryption will have a bit of overlap with the encryption when
# using a standard keyboard and not assigning ASCII or unicode symbols to each letter. I don't have enough time to
# troubleshoot the cipher so it'll have to stay like this. Outputted file is a bit wonky but its relatively readable.

def main():
    cryptogram_key_dct = {'a': '%', 'c': '!', 'b': 'T', 'e': '*', 'd': '3', 'g': '@', 'f': '#', 'i': 'r', 'h': 'G',
                          'k': '&',
                          'j': 'y', 'm': '6', 'l': 'V', 'o': 'U', 'n': 'E', 'q': 'I', 'p': 'A', 's': 'M', 'r': '^',
                          'u': 'Q',
                          't': '-', 'w': '_', 'v': '=', 'y': '+', 'x': 'F', 'z': '~'}

    # taking the cryptogram key and reversing the key:value pairs to give a dictionary to decrypt a file encrypted with
    # the cryptogram dictionary
    decrypt_key_dct = {value: key for (key, value) in cryptogram_key_dct.items()}

    user_file = input('What is the name of the file you are looking to decrypt? ')
    infile = open(user_file, 'r')

    decrypted_file = open('decrypted.txt', 'w')

    for line in infile:
        for ch in line:
            if ch not in decrypt_key_dct:
                decrypted_file.write(ch)
            else:
                decrypted_ch = decrypt_key_dct[ch]
                decrypted_file.write(decrypted_ch)


main()

#######################################################################################################################
# 4. Unique Words.


# it just struck me while doing #5 that I could have used the split function to take the words from the file.
# would have been more computationally efficient.

def main():
    user_file = input('Please enter the name of your text file and the program will return the amount of unique words. ')
    # opening file
    infile = open(user_file, 'r')
    # creating a set
    set_of_words = set()
    # creating a string for holding words
    holding_string = ''

    # taking each line in the file
    for line in infile:
        # stripping new line
        line = line.rstrip('\n')
        # taking each character in the line
        for ch in line:
            # if a space is found, the holding string will be dumped into the set
            if ch == ' ':
                set_of_words.add(holding_string)
                holding_string = ''
                pass
            # otherwise the character will be added to the word
            else:
                holding_string += ch
    # printing the length of set, aka the unique word count
    print('The amount of unique words in the text file is', len(set_of_words))


main()
