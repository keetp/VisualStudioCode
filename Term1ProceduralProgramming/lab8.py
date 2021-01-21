# 1. Initials. User enters their full name, initials are printed out.

def main():
    # asking user for their name
    user_name = input('What is your full name? Include your middle name. ')
    # initializing the first character in the initials, which will be the first index of the string. Adding a period
    # and a space for formatting.
    initials = user_name[0] + '. '
    # iterating over the length of the string
    for i in range(len(user_name)):
        # if a space is found
        if user_name[i] == ' ':
            # append the next character after the space to the initials. again period+space for formatting
            initials += user_name[i + 1] + '. '
    # after the loop is exhausted, print
    print(initials)


# calling main
main()


#######################################################################################################################
# 2. Sum of Digits in a String. User enters a string containing a series of single-digit numbers with nothing
# separating them.

def main():
    # asking for user input
    series_of_numbers = input('Please input a series of single digits. No spaces. ')
    # initializing
    sum_of_digits = 0
    # iterating through the string
    for i in series_of_numbers:
        # converting the string character to an integer and adding to sum
        sum_of_digits += int(i)
    # printing sum
    print(sum_of_digits)


main()


#######################################################################################################################
# 3. Date Printer. User enters a date in form mm/dd/yyyy. Program prints out the date in words.

def main():
    # variable for the user inputted string
    date = input('Enter a date in the form mm/dd/yyyy: ')
    month = ''
    # converting the month section of the inputted date to the month name
    if date[0:2] == '01':
        month = 'January'
    elif date[0:2] == '02':
        month = 'February'
    elif date[0:2] == '03':
        month = 'March'
    elif date[0:2] == '04':
        month = 'April'
    elif date[0:2] == '05':
        month = 'May'
    elif date[0:2] == '06':
        month = 'June'
    elif date[0:2] == '07':
        month = 'July'
    elif date[0:2] == '08':
        month = 'August'
    elif date[0:2] == '09':
        month = 'September'
    elif date[0:2] == '10':
        month = 'October'
    elif date[0:2] == '11':
        month = 'November'
    elif date[0:2] == '12':
        month = 'December'

    # printing date in the proper format to the user
    print(month, date[3:5] + ',', date[6:10])


main()


#######################################################################################################################

# 4. Morse Code Converter. User enters a string, program pumps out a morse code.

def main():
    morse_code_list = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-',
                       '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                       '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..', '--.--',
                       '.-.-.-', '..--..', ' ']
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', ',', '.', '?', ' ']
    morse_code_string = ''
    user_string = input('What phrase would you like converted to morse code? ')

    for i in user_string:
        if i in alphabet:
            morse_code_index = alphabet.index(i)
            morse_code_string += morse_code_list[morse_code_index] + ' '

    print(morse_code_string)


main()


#######################################################################################################################

# 5. Alphabetic Telephone Number Translator. A phone number containing alphabet characters is entered, the program
# converts the number to a full digit phone number.

def main():
    # asking for a phone number from user
    phone_number_alpha = input('Please enter a phone number in the form XXX-XXX-XXXX that you wish '
                               'converted to all digits: ')
    # holding string for the decimal converted number
    phone_number_deci = ''
    # iterating through the phone number and changing alphabet characters to decimal digits based on the given
    # guidelines in the book
    for i in phone_number_alpha:
        # making sure the examined character is an uppercase
        i = i.upper()
        if i == 'A' or i == 'B' or i == 'C':
            phone_number_deci += '2'
        elif i == 'D' or i == 'E' or i == 'F':
            phone_number_deci += '3'
        elif i == 'G' or i == 'H' or i == 'I':
            phone_number_deci += '4'
        elif i == 'J' or i == 'K' or i == 'L':
            phone_number_deci += '5'
        elif i == 'M' or i == 'N' or i == 'O':
            phone_number_deci += '6'
        elif i == 'P' or i == 'W' or i == 'R' or i == 'S':
            phone_number_deci += '7'
        elif i == 'T' or i == 'U' or i == 'V':
            phone_number_deci += '8'
        elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            phone_number_deci += '9'
        else:
            # if no alphabet characters are found, whatever number is in the string gets appended
            phone_number_deci += i

    # printing phone number to user
    print('Your phone number,', phone_number_alpha, 'entirely in digits is', phone_number_deci)


# calling main
main()


#######################################################################################################################
# 6. Average Number of Words. Finds the average number of words per line in a file.

def main():
    # opening the text file
    infile = open('text.txt', 'r')
    # initializing the counter
    word_count = 0
    # calling line_counter function to get total lines in the file
    num_lines = line_counter('text.txt')
    # for each line in the file
    for line in infile:
        # splitting the sentences
        words_in_line = line.split()
        # getting the word count of each split
        word_count += len(words_in_line)
    # printing average
    print('The average number of words per line in the text.txt file is', word_count / num_lines)
    infile.close()


# function to count all the lines in the file.
def line_counter(filename):
    # variable for the file, opening it in read mode
    file = open(filename, 'r')
    # initializing the counting variable
    line_count = 0
    # going through each line in the file
    for line in file:
        # accumulating the line counter if there is content to be found on the file line.
        if line != "\n":
            line_count += 1
    # closing the file
    file.close()
    # returning the line counter
    return line_count


main()


#######################################################################################################################
# 7. Character Analysis. Getting the count of uppercases, lowercases, digits and spaces.

def main():
    # opening file
    infile = open('text.txt', 'r')
    # initializations
    upper_counter = 0
    lower_counter = 0
    digit_counter = 0
    space_counter = 0
    # for each line in the file
    for line in infile:
        # for each character in the line
        for ch in line:
            # counting the uppers, lowers, digits and the spaces
            if ch.isupper():
                upper_counter += 1
            elif ch.islower():
                lower_counter += 1
            elif ch.isdigit():
                digit_counter += 1
            elif ch == ' ':
                space_counter += 1
    # printing the counts to the user
    print('The amount of upper-case characters is', upper_counter)
    print('The amount of lower-case characters is', lower_counter)
    print('The amount of digits in the file is', digit_counter)
    print('The amount of blank spaces in the file is', space_counter)
    # closing the file
    infile.close()


main()


#######################################################################################################################

# 8. Sentence Capitalize. Properly capitalizing a sentence that's inputted with punctuation.

def main():
    # asking for user input
    user_string = input('What do you want in real english? Use punctuation you fool. ')
    # initializations
    holding_list = []
    list_string = ''
    capitalized_string = ''
    # for each character in the string
    for i in user_string:
        # if punctuation is found, string is appended to a list
        if i == '.' or i == '!' or i == '?':
            list_string += i
            holding_list.append(list_string)
            # string is emptied
            list_string = ''
        else:
            list_string += i
    # for each element in the list
    for x in holding_list:
        # stripping the blank space at the left of the string
        x = x.lstrip(' ')
        # setting the capitalized string with proper capitalization after the punctuation
        capitalized_string += x[0].upper() + x[1:] + ' '
    # printing the fixed string
    print(capitalized_string)


main()


#######################################################################################################################

# 9. Vowel and Consonant Count. User inputs a string. Program counts the vowels and the consonants in the string.

def main():
    # getting user input
    print('This program will count the number of consonants and vowels in a given sentence.')
    user_string = input('Please enter the sentence you wish to have the vowels/consonants counted in: ')
    # calling the consonant counter and the vowel counter functions to print to the user
    print('# of consonants: ', consonant_counter(user_string))
    print('# of vowels: ', vowel_counter(user_string))


# function for counting the consonants in an inputted string. compares the inputted string to a list of consonants.

def consonant_counter(string):
    consonant_list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
                      'X', 'Z', 'Y']
    # initializing accumulator
    count = 0
    # making the inputted string all uppercase for comparison to list
    string = string.upper()
    for i in string:
        # if the character in the string is in the list, accumulator goes up by 1.
        if i in consonant_list:
            count += 1
    # returns accumulator
    return count


# function for counting the vowels in an inputted string. compares the inputted string to a list of vowels.

def vowel_counter(string):
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    # initializing accumulator
    count = 0
    # making the inputted string all uppercase for comparison to list
    string = string.upper()
    for i in string:
        # if the character in the string is in the list, accumulator goes up by 1.
        if i in vowel_list:
            count += 1
    # returns accumulator
    return count


main()


#######################################################################################################################
# 10. Character Counter. A string is inputted. The program returns which character appears the most in the inputted
# string


def main():
    # asking for user input
    user_string = input('Enter a sentence and the program will tell you which character is most often used and the '
                        'frequency of occurences: ')
    # initializations
    number_of_occurrences = 0
    most_frequent = ''
    # going through each character, lower() is used to ensure capitals and lower case are not counted separate
    for i in user_string.lower():
        # getting the count of each character in the string
        ch_count = user_string.count(i)
        # passing if a space is found. remove this line if you want to count spaces
        if i == ' ':
            pass
        # if the character count found is more than the highest character count found so far
        elif ch_count > number_of_occurrences:
            # setting the new most occurring character to the variables
            most_frequent = i
            number_of_occurrences = ch_count
    # printing to user
    print('The most common occurring character is', most_frequent)
    print('The number of times it occurs is', number_of_occurrences)


main()


#######################################################################################################################

# 11. Word Separator. A string with no spaces and only capitals is inputted. Spaces are placed at the place of the
# capitals

def main():
    # user input
    user_string = input('What sentence do you wish to separate? ')
    # initializations
    new_list = []
    # putting the first character in the string as the start of the string to be appended to the holding list
    holding_string = user_string[0]
    corrected_string = ''
    # for every character past the first character
    for i in user_string[1:]:
        # if an upper case is found
        if i.isupper():
            # append the string to the list
            new_list.append(holding_string)
            # empty the string
            holding_string = ''
            # starting next holding string
            holding_string += i.lower()
        else:
            # adding to the holding string
            holding_string += i
    # final string being appended
    new_list.append(holding_string)
    # for each element in the list
    for x in new_list:
        # put into a string and a space
        corrected_string += x + ' '
    # printing to user
    print('The corrected string with proper spaces and uppercases:', corrected_string)


main()


#######################################################################################################################
# 12. Pig Latin.

def main():
    # taking the user input and splitting it
    split_string = str(input("Please enter a sentence. The return sentence will be your sentence "
                             "but in Pig Latin: ")).split()
    # for each word in the split
    for string in split_string:
        # pig latin
        print(string[1:] + string[0] + "ay", end=" ")


main()
