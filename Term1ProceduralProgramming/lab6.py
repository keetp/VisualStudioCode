# importing library for future use
import random


# 1. File Display. There exists a file named numbers.txt that contains a list of integers. The program displays
# all of the integers that appear in the file.

def main():
    # opening the numbers.txt file in read-mode
    infile = open('numbers.txt', 'r')
    # printing the contents of the numbers.txt file
    print(infile.read())
    # closing the numbers.txt file
    infile.close()


# calling the main function
main()


#######################################################################################################################

# 2. File Head Display. The program asks the user what the name of the file is, and then returns the first 5 lines
# of the file. If there is not more than 5 lines, the entire file is displayed.

def main():
    # retrieving the name of the file from the user and assigning to user_file
    user_file = input('Enter the name of your text file. Do not include the .txt extension: ')
    # taking the user's file name and opening the file in read mode
    infile = open(user_file + '.txt', 'r')
    # looping 5 times, with each iteration printing a line from the user's file
    for i in range(5):
        print(infile.readline(), end='')

    # closing the file
    infile.close()


# calling main function
main()


#######################################################################################################################

# 3. Line Numbers. Gets a filename from a user and prints the content of the file line by line, preceding
# with a line number and a colon.

def main():
    # initializing the variable that will be used to count the line number
    line_number = 0
    # asking user for file name input, asking to leave out the .txt as we add it in later.
    user_file = input('Please enter the name of your file. Do not include the .txt extension: ')
    # opening the user's file in read-mode
    infile = open(user_file + '.txt', 'r')

    # loop that will iterate through each line in the user file
    for line in infile:
        # accumulator for counting line number
        line_number += 1
        # printing the line number, a colon and the line content
        print(str(line_number) + ':', line, end='')
    # printing new line for formatting purposes in the next program being ran
    # was having display issues where the last line would run into the next program
    print('\n')
    # closing the file
    infile.close()


# calling main function
main()


#######################################################################################################################

# 4. Item Counter. A file contains a series of names as strings. The program counts how many lines total are in
# the file.

def main():
    # setting a variable to the name of the file
    user_file = 'names.txt'
    # opening the file in read-mode
    infile = open(user_file, 'r')
    # initializing a counter to keep track of how many lines are in the file
    line_counter = 0

    # for loop that iterates through each line in the file
    for line in infile:
        # accumulating the line counter for each line that is iterated through
        line_counter += 1

    # printing the total number of lines within the given file
    print('There are', line_counter, 'strings in the file', user_file)
    # closing the file
    infile.close()


# calling main function
main()


#######################################################################################################################

# 5. Sum of Numbers. A file contains a series of integers. The program reads the file and sums the integers that are on
# the file.

def main():
    # variable that holds the file name
    file_name = 'numbers.txt'
    # opening the file in read-mode
    infile = open(file_name, 'r')
    # initializing the holding variable for the sum
    total_sum = 0

    # iterating through each line in the file
    for line in infile:
        # when each line is retrieved, it is set as an integer so the compiler can add them
        line_number = int(line)
        # adding each integer in the line to the holding variable containing the sum
        total_sum += line_number

    # closing the file
    infile.close()
    # printing the total sum
    print('The series total of the integers stored on', file_name, 'is', total_sum)


# calling the main function
main()


#######################################################################################################################

# 6. Average of Numbers. A file contains a series of integers. The program takes the integers and calculates
# the average.

def main():
    # variable that holds the file name
    file_name = 'numbers.txt'
    # opening the file in read-mode
    infile = open(file_name, 'r')
    # initializing the holding variable for the sum
    total_sum = 0
    # initializing the counter for how many lines are contained in the file
    line_counter = 0

    # iterating through each line in the file
    for line in infile:
        # when each line is retrieved, it is set as an integer so the compiler can add them
        line_number = int(line)
        # adding each integer in the line to the holding variable containing the sum
        total_sum += line_number
        line_counter += 1

    # closing the file
    infile.close()

    # calculating the average using the sum divided by the number of lines
    average = round((total_sum / line_counter), 2)
    # printing the total sum
    print('The average of the integers on the file', file_name, 'is',
          average)


# calling the main function
main()


#######################################################################################################################

# 7. Random Number File Writer. User inputs how many numbers they want added to a file. The program creates that
# amount of random numbers and stores them in the file.

def main():
    print('This program will store a given amount of random numbers on a file.')
    # asking the user how many numbers they would like written to the file and setting it to a variable
    numbers_on_file = int(input('How many random numbers do you want to have on the file? '))
    # creating and opening the file in write-mode
    outfile = open('randomNumbers.txt', 'w')

    # loop that iterates the number of inputted times
    for line in range(numbers_on_file):
        # generating a random integer between 1 and 500
        random_number = random.randint(1, 500)
        # writing the random number onto the file
        outfile.write(str(random_number) + '\n')

    # closing the file
    outfile.close()


# calling the main function
main()


#######################################################################################################################

# 8. Random Number File Reader. Takes the file written in #7 containing a series of random numbers, prints all the
# numbers contained on the file, prints the sum of all the numbers, and prints the amount of numbers on the file.

def main():
    # initializing the variable holding the sum of the numbers
    sum_of_numbers = 0
    # initializing the variable holding the number of lines
    line_counter = 0
    # setting the file name to a variable
    file_name = 'randomNumbers.txt'
    # opening the file in read-mode
    infile = open(file_name, 'r')
    # alerting the user to what is about to be printed
    print('The following numbers are contained on the randomNumbers.txt file: ')

    # iterates for each line contained in the file
    for line in infile:
        # prints each line as it is read
        print(line, end='')
        # adds the value contained in the file to the variable holding the running total of the sum
        sum_of_numbers += int(line)
        # adds 1 to the counter for each line read
        line_counter += 1

    # prints the sum of the numbers on the file
    print('The sum of all the numbers on the file is', sum_of_numbers)
    # prints the amount of lines in the file
    print('The amount of lines in the file is', line_counter)

    # closing the file
    infile.close()


# calling main function
main()


#######################################################################################################################

# 9. Exception Handling. Modified version of the program in #6 to handle errors.

def main():
    try:
        # variable that holds the file name
        file_name = 'numbers.txt'
        # opening the file in read-mode
        infile = open(file_name, 'r')
        # initializing the holding variable for the sum
        total_sum = 0
        # initializing the counter for how many lines are contained in the file
        line_counter = 0

        # iterating through each line in the file
        for line in infile:
            # when each line is retrieved, it is set as an integer so the compiler can add them
            line_number = int(line)
            # adding each integer in the line to the holding variable containing the sum
            total_sum += line_number
            line_counter += 1

        # closing the file
        infile.close()

        # calculating the average using the sum divided by the number of lines
        average = round((total_sum / line_counter), 2)
        # printing the total sum
        print('The average of the integers on the file', file_name, 'is',
              average)
    # error message in the case that the program returns an IOError
    except IOError:
        print('ERROR: File could not be properly read. Make sure the file is in the specified directory.')
    # error message in the case that the program returns a ValueError
    except ValueError:
        print('ERROR: Program attempted to read a non-number as a number.')


# calling the main function
main()


#######################################################################################################################

# 10a. Golf Scores part a. The user enters a players name and their golf score as an input. The program writes these
# inputs to a file named golf.txt and then asks the user if they wish to continue

def main():
    # variable that controls if the while loop continues or not
    more_names = 'y'
    # initialization of player's name variable
    player_name = ''
    # initialization of player's score variable
    player_score = 0
    # creating and opening the golf.txt file
    outfile = open('golf.txt', 'w')
    print('The following program will store a player name and a golf score for the player.')
    # continues while the controlling variable is set at 'y' for yes
    while more_names == 'y' or more_names == 'Y':
        # asking the user for player name input
        print("Please enter the player's name: ")
        player_name = str(input())
        # asking the user for player score input
        print("Please enter the player's score: ")
        player_score = str(input())

        # writing the player's name and player's score to the file, tab indentation added for formatting
        outfile.write(player_name + ';\t' + player_score + '\n')

        # asking the user if they would like to enter more values
        print('Do you wish to add more values? (y = yes, anything else = no)')
        more_names = input()
    # closing the file
    outfile.close()


# calling main function
main()


#######################################################################################################################

# 10b. Golf Scores part b. Program to read and display the golf names and scores.

def main():
    # opening the golf.txt file
    infile = open('golf.txt', 'r')
    # giving the user information on what is about to be printed
    print("The player's name and the player's score are as follows:")
    # printing the contents of the golf.txt file
    print(infile.read())
    # closing the file
    infile.close()


# calling main function
main()


#######################################################################################################################

# 11. Personal Web Page Generator. Program asks for user's name and description and creates a simple html webpage,
# formatted for the user.

def main():
    # creating a new html file named webpage.html, opening it in write-mode
    outfile = open('webpage.html', 'w')
    # alerting user about what the program will do
    print('The following program builds a small html webpage based on the given information.')
    # asking user for their name
    user_name = str(input('Enter your name: '))
    # asking user for a brief description of themselves
    user_description = str(input('Describe yourself: '))
    # formatting according to the textbook's html example. string literal \n = new line, \t = indent,
    # \r = carriage reset. takes the user input variables and places them in the proper spot
    html_code = ("<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>" + user_name +
                 "</h1>\n\r\t</center>\n\t<hr />\n\t" +
                 user_description + "\n\t<hr />\n\r</body>\n</html>")

    # takes the formatted string and writes it to the file
    outfile.write(html_code)
    # closing file
    outfile.close()


# calling main function
main()


#######################################################################################################################

# 12. Steps taken. A file named steps.txt has 365 for each day of the year, representing the amount of steps someone
# had taken on that day. Program opens the file and prints the average steps a day for each month.

# Since the file has to be read in order, the program will take data from the file in chunks, each chunk being the
# amount of days in the month. Since it needs to be done in succession in order for the readline function to save the
# position, it will all be done in the main function.
def main():
    # opening the file steps.txt
    infile = open('steps.txt', 'r')
    # initializing holding variable for the running total for each month
    running_total = 0

    # beginning the data extraction starting at January. Each loop is identical, minus the naming of the variables
    # to keep me from getting lost and the amount of days. Each loop reads one line for each day in the month, strips
    # the new line command, converts the extracted value to an int and adds it to the running total. I won't be
    # explicitly commenting each loop to save space and keep things clean. Loops are titled by month.

    # average for january
    for i in range(1, 32):
        january = infile.readline()
        january = january.rstrip('\n')
        running_total += int(january)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during January is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for february
    for i in range(1, 29):
        feb = infile.readline()
        feb = feb.rstrip('\n')
        running_total += int(feb)

    # calculating average per day for the month
    average_steps = running_total / 28
    # informing user of the calculated average
    print('The average steps a day during February is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for march
    for i in range(1, 32):
        march = infile.readline()
        march = march.rstrip('\n')
        running_total += int(march)

    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during March is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for april
    for i in range(1, 31):
        april = infile.readline()
        april = april.rstrip('\n')
        running_total += int(april)

    # calculating average per day for the month
    average_steps = running_total / 30
    # informing user of the calculated average
    print('The average steps a day during April is:', format(average_steps, '.1f'))

    # reinitializing

    running_total = 0

    # average for may
    for i in range(1, 32):
        may = infile.readline()
        may = may.rstrip('\n')
        running_total += int(may)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during May is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for June
    for i in range(1, 31):
        june = infile.readline()
        june = june.rstrip('\n')
        running_total += int(june)

    # calculating average per day for the month
    average_steps = running_total / 30
    # informing user of the calculated average
    print('The average steps a day during June is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for July
    for i in range(1, 32):
        july = infile.readline()
        july = july.rstrip('\n')
        running_total += int(july)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during July is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for August
    for i in range(1, 32):
        august = infile.readline()
        august = august.rstrip('\n')
        running_total += int(august)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during August is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for september
    for i in range(1, 31):
        sept = infile.readline()
        sept = sept.rstrip('\n')
        running_total += int(sept)

    # calculating average per day for the month
    average_steps = running_total / 30
    # informing user of the calculated average
    print('The average steps a day during September is:', format(average_steps, '.1f'))
    # reinitializing
    running_total = 0

    # average for october
    for i in range(1, 32):
        october = infile.readline()
        october = october.rstrip('\n')
        running_total += int(october)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during October is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for november
    for i in range(1, 31):
        nov = infile.readline()
        nov = nov.rstrip('\n')
        running_total += int(nov)

    # calculating average per day for the month
    average_steps = running_total / 30
    # informing user of the calculated average
    print('The average steps a day during November is:', format(average_steps, '.1f'))

    # reinitializing
    running_total = 0

    # average for december
    for i in range(1, 32):
        dec = infile.readline()
        dec = dec.rstrip('\n')
        running_total += int(dec)

    # calculating average per day for the month
    average_steps = running_total / 31
    # informing user of the calculated average
    print('The average steps a day during December is:', format(average_steps, '.1f'))
    # closing the file
    infile.close()


main()
