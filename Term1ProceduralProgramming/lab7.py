# 1. Total sales. User enters sale information for each day of the week. The information is stored in a list, tallied
# and returned to user after all the inputs are entered.
def main():
    # initializations
    total_sales = 0  # accumulator
    number_of_days = 7  # number of days being inputted.
    # creating the list that will hold the sales information
    sales = [0] * number_of_days
    for i in range(number_of_days):
        # using the number_to_day function to tell user what day of the week is being inputted
        day_name = number_to_day(i)
        print('Sales for', day_name)

        # asking the user for input
        sales[i] = float(input())
        # accumulation of the inputted sales values to print the total week sales
        total_sales += sales[i]

    # printing total sales to two decimal places
    print('Total sales for the week: $', format(total_sales, '.2f'))


# a function to convert an int input to a day name. 0=monday, 1=tuesday and so on. used to display day names inside
# of a loop. mod 7 for the 7 days in the week.
def number_to_day(int):
    if int % 7 == 0:
        return 'Monday'
    elif int % 7 == 1:
        return 'Tuesday'
    elif int % 7 == 2:
        return 'Wednesday'
    elif int % 7 == 3:
        return 'Thursday'
    elif int % 7 == 4:
        return 'Friday'
    elif int % 7 == 5:
        return 'Saturday'
    elif int % 7 == 6:
        return 'Sunday'
    # error statement if the int is outside of expected range.
    else:
        return 'ERROR: input was unexpected'


main()

#######################################################################################################################
# 2. Lottery Number Generator.
# importing random library
import random


def main():
    # initializing the list that holds the lottery number
    lottery_numbers = [0] * 7
    # loop that will generate a random number between 0 and 9 and places them in the list.
    for i in range(7):
        lottery_numbers[i] = random.randint(0, 9)

    # alerting user of what will be printed
    print('Your lottery numbers is:')
    # reading the contents of the list with no newlines or separations
    for x in range(7):
        print(lottery_numbers[x], end='')


main()


#######################################################################################################################

# 3. Rainfall Statistics. Gets user input for rainfall data on each of the months of the year. Prints total rainfall,
# average rainfall, highest rainfall and lowest rainfall.

def main():
    # initializing list for rainfall values
    rainfall_per_month = [0] * 12
    # initializing accumulator for total rainfall
    total_rainfall_annual = 0

    # retrieving user input and storing in each element of the list
    for i in range(12):
        print('\nMonth', i + 1)
        rainfall_per_month[i] = float(input('Total rainfall for this month: '))

    # summing the values contained in the list
    for x in range(12):
        total_rainfall_annual += rainfall_per_month[x]

    # print statements with the total, average, max and min rainfalls
    print('The total annual rainfall is ', total_rainfall_annual)
    print('The average monthly rainfall is ', format(total_rainfall_annual / 12, '.2f'))
    print('The highest rainfall over the course of 12 months was', format(max(rainfall_per_month), '.2f'))
    print('The lowest rainfall over the course of 12 months was', format(min(rainfall_per_month), '.2f'))


main()


#######################################################################################################################

# 4. Number Analysis Program. Gets a user to input 20 numbers, holds the numbers in a list and then displays the
# lowest number, the highest number, the total of the numbers and the average of the numbers.

def main():
    # initializations
    number_list = [0] * 20
    total_of_list = 0  # holding value for the total
    # warning the user of what is happening
    print('You will be entering 20 numbers, so prepare yourself!')

    # loop to take user input 20 times
    for i in range(20):
        user_number = float(input('Please enter a number: '))
        # assigning user input to the ith list element
        number_list[i] = user_number
        # adding the user input to the total
        total_of_list += user_number

    # maximum number in the list
    highest_number = max(number_list)
    # minimum number in the list
    lowest_number = min(number_list)
    # print statements containing the lowest number, highest number, average of the list and the total of the list
    print('The lowest number in the list is', lowest_number)
    print('The highest number in the list is', highest_number)
    print('The average of the numbers in the list is', format(total_of_list / 20, '.2f'))
    print('The total of the numbers in the list is', total_of_list)


main()


#######################################################################################################################

# 5. Charge Account Validation. A list is created from the file charge_accounts.txt. The user enters an account number
# and the program checks if the account number is present in the list.

def main():
    # initializations

    # variable to keep track of which index is being read
    list_index = 0
    # user file
    user_filename = 'charge_accounts.txt'
    # opening the file
    infile = open('charge_accounts.txt', 'r')
    # calling the line counter function to get the number of lines
    number_of_lines = line_counter(user_filename)
    # initializing the list that the file content will be held
    charge_accounts = [0] * number_of_lines
    # asking user for an account number to check for existence
    user_account_number = int(input('What account number are you looking for? '))

    # going through each line in the file in a loop
    for line in infile:
        # setting each line's account number to an integer and holding it in a variable
        account_number = int(line)
        # adding the account number to the list
        charge_accounts[list_index] = account_number
        # accumulating the index by 1
        list_index += 1

    # calling the account number search function to check for the user's account number within the charge accounts list.
    # if the function returns True, the account number is valid. Otherwise, the account number is not valid.
    if account_number_search(charge_accounts, user_account_number) is True:
        print('The account number is valid.')
    else:
        print('The account number is not valid.')


# function to count the number of lines in a file
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


# function to find if a particular element is in a list
def account_number_search(list, account_number):
    # iterating through the length of the list
    for i in range(len(list)):
        # checking each individual element for a match
        if list[i] == account_number:
            # returns True if found
            return True
    # otherwise returns False
    return False


main()


#######################################################################################################################

# 6. Larger Than n. Function which takes a number n and a list and then returns
# a list containing all numbers that are bigger than n on the inputted list.

# unsure if this portion is necessary as it is just a way for me to test the created function, but I'm gonna include it
# anyways.
def main():
    # building a test list to test out the function larger_than_n.
    numbers_list = [0] * 20
    for i in range(20):
        numbers_list[i] = i
    # testing the function
    big_numbers = larger_than_n(5, numbers_list)
    print(big_numbers)


# function which takes a number n and a list, and then returns a second list that contains all the numbers bigger than
# n on the list taken as an argument.
def larger_than_n(n, list):
    # holding list for the numbers bigger than n
    larger_numbers = []
    # running through each element in the inputted list
    for i in range(len(list)):
        # if n is less than the element of list
        if n < list[i]:
            # append the number to the list of the bigger numbers.
            larger_numbers.append(list[i])
        else:
            # otherwise continue with the loop
            pass
        # return the list of larger than n numbers
    return larger_numbers


main()


#######################################################################################################################
# 7. Driver's License Exam. A file of answers to a test is somewhere on a system. the file is read into a list and
# compared to a list of the correct answers. program will tell the user how many questions are right, wrong and if
# they passed/failed.

def main():
    # initializations
    # accumulator for going through the list while having the for loop go through the opened file
    i = 0
    # two holding variables for the total correct answers and total incorrect answers. will be accumulated.
    total_correct = 0
    total_incorrect = 0
    # holding list for the incorrect answers to be appended to
    incorrect_list = []
    # the given answer scheme
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D',
                       'A']
    # list for the student answers
    student_answers = [0] * 20
    # opening the text file with the student answers on it
    infile = open('answers.txt', 'r')

    # going through each line in the
    for line in infile:
        # stripping the new file character from the txt file
        line = line.strip('\n')
        # putting the stripped line into a list
        student_answers[i] = line
        # accumulating i
        i += 1

    # going through each element in each list and comparing them
    for x in range(20):
        # if the student answer matches the correct answer
        if student_answers[x] == correct_answers[x]:
            # accumulating total correct variable
            total_correct += 1
        else:
            # accumulating total incorrect variable
            total_incorrect += 1
            # appending the wrong question number to a list
            incorrect_list.append(x)

    # print statements telling the user how many incorrect, how many correct and the list of the questions
    # answered incorrectly. If the total incorrect is more than 5, the user has failed the exam and will inform him so
    print('The total number of correct answers is', total_correct)
    print('The total number of incorrect answers is', total_incorrect)
    print('The questions you got wrong are as follows: ')
    print(incorrect_list)
    if total_incorrect > 5:
        print('You have failed your driver exam.')

    infile.close()


main()


#######################################################################################################################
# 8. Name Search. Two text files containing popular baby names are opened. a user enters a name and the program checks
# to see if the name exists on one of the files.

def main():
    # calling the file to list function to put the data found on both boy names and girl names text files to lists
    boy_name_list = file_to_list('BoyNames.txt')
    girl_name_list = file_to_list('GirlNames.txt')
    # alerting user of what the program does
    print('You will be given the option to enter a boy/girl name to search among the top 200 names. ')
    # asking if they wish to search for a boy's name
    boy_input_confirmation = input('Do you wish to enter a boy name to search for? (y/Y for yes) ')
    # if the input was yes, the program will ask for the boy name from the user and assign it to a variable
    if boy_input_confirmation == 'y' or boy_input_confirmation == 'Y':
        boy_input = input('What boy name do you wish to search for? Be sure to capitalize. ')
        # running the inputted boy name into the name search function, which returns that the name was found if it was,
        # and if not returns that the name was not found
        print(name_search(boy_input, boy_name_list))
    # asking if they wish to search for a girl's name
    girl_input_confirmation = input('Do you wish to enter a girl name to search for (y/Y for yes)? ')
    # if the input was yes, the program will ask for the girl name from the user and assign to a variable
    if girl_input_confirmation == 'y' or girl_input_confirmation == 'Y':
        girl_input = input('What girl name do you wish to search for? Be sure to capitalize. ')
        # running the inputted girl name into the name search function
        print(name_search(girl_input, girl_name_list))


# a function to search for existence of a name on a list. the function iterates through each element in the list and
# compares it to the name that was inputted.
def name_search(name, list):
    # iterating the length of the list
    for i in range(len(list)):
        # setting the current element to a variable
        current_name = list[i]
        # comparing the variable to the inputted name. if it is match, the function returns that the name was found.
        if current_name == name:
            return 'Name has been found!'
        else:
            # if not contines to the next element
            pass
    # it name was not found through all iterations, returns that the name wasnt found
    return 'Name has not been found.'


# a function to convert an inputted file into a list
def file_to_list(file):
    # initializing a list
    return_list = []
    # opening the file in read mode
    infile = open(file, 'r')
    # iterating through each line in the list
    for line in infile:
        # stripping the new line
        line = line.strip('\n')
        # appending to the list that will be returned
        return_list.append(line)
    # closing the file
    infile.close()
    # returns the built list containing the names
    return return_list


main()


#######################################################################################################################
# 9. Population Data. Population data is held on a text file. The program gives the user average rate of change,
# the year with the biggest increase and the year with the smallest increase.

def main():
    # initializations
    population_change_list = []
    max_index = 0
    min_index = 0
    # calling the file to list function to convert the population data on the text file into a list
    us_population_list = file_to_list('USPopulation.txt')
    # calculating average rate of change by taking the last element minus the first element and dividing by the length
    # of the list
    average_total_increase = (int(us_population_list[len(us_population_list) - 1]) - int(us_population_list[0])) / len(
        us_population_list)
    # printing average change to user
    print('The average annual population increase from 1950 to 1990 in the US was',
          format(average_total_increase, '.1f'), 'people per year.')

    # calculating the change from year to year and putting the data into a list. will contain one less element than the
    # original population list.
    for i in range(1, len(us_population_list)):
        population_change = int(us_population_list[i]) - int(us_population_list[i - 1])
        population_change_list.append(population_change)

    # max and min of the list of population change to find which years had the biggest and smallest change and
    # assigning to a variable
    max_population_change = max(population_change_list)
    min_population_change = min(population_change_list)

    # going through the list of population change to find where the max/min are located. the loop weights the max/min
    # against the element that is currently being examined, and if found to be equal to the max, stores the index in
    # a variable
    for x in range(len(population_change_list)):
        current_population_change = population_change_list[x]
        if current_population_change == max_population_change:
            max_index = x
        if current_population_change == min_population_change:
            min_index = x

    # printing the year which the smallest change and biggest change happened.
    print('The year with the biggest change in population happened from', max_index + 1950, 'to', max_index + 1951)
    print('The year with the smallest change in population happened from', min_index + 1950, 'to', min_index + 1951)


# a function to convert an inputted file into a list. same one as used above, including just to keep the questions
# straight
def file_to_list(file):
    # initializing a list
    return_list = []
    # opening the file in read mode
    infile = open(file, 'r')
    # iterating through each line in the list
    for line in infile:
        # stripping the new line
        line = line.strip('\n')
        # appending to the list that will be returned
        return_list.append(line)
    # closing the file
    infile.close()
    # returns the built list containing the names
    return return_list


main()


#######################################################################################################################
# 10. World Series Winners. user enters the name of a baseball team. the program prints how many world series inputted
# team has won.

def main():
    # calling the file to list function to convert the data in the text file to a list
    world_series_winners = file_to_list('WorldSeriesWinners.txt')
    users_team = input('This program will tell you how many World Series a team has won in the last 100 years.\n'
                       'Which team would you like to search for? ')
    print('The', users_team, 'have won the World Series', world_series_winners.count(users_team), 'times.')


# a function to convert an inputted file into a list. same one as used above, including just to keep the questions
# straight
def file_to_list(file):
    # initializing a list
    return_list = []
    # opening the file in read mode
    infile = open(file, 'r')
    # iterating through each line in the list
    for line in infile:
        # stripping the new line
        line = line.strip('\n')
        # appending to the list that will be returned
        return_list.append(line)
    # closing the file
    infile.close()
    # returns the built list containing the names
    return return_list


main()


#######################################################################################################################
# 11. Lo Shu Magic Square. function which checks if an inputted 3x3 2d list is a Lo Shu magic square or not.

# test list
def main():
    list2d = [[4, 9, 2],
              [3, 5, 7],
              [8, 1, 6]]
    lo_shu_magic_square(list2d)


# function to check and see if an inputted 3x3 2d list is a lo shu magic square. probably should've broken this up into
# multiple functions. didn't realize how cumbersome it looked until i finished.
def lo_shu_magic_square(two_d_list):
    # initializations of holding lists for the row sums and column sums
    row_sums = [0, 0, 0]
    col_sums = [0, 0, 0]
    # initializing a list to convert the 2d list into a 1d list
    conversion1d_list = []
    # nested loop to go through each element in the 2d list
    for j in range(len(two_d_list)):
        for i in range(len(two_d_list)):
            # calculating row sum and column sum and placing them into their holding lists
            row_sums[i] += two_d_list[i][j]
            col_sums[i] += two_d_list[j][i]
            # appending the element from the 2d list to a 1d list
            conversion1d_list.append(two_d_list[i][j])
            # adding a clause that the element must be an integer from 1-9. if found to be outside of the range, the
            # program will terminate.
            if int(two_d_list[i][j]) > 9 or int(two_d_list[i][j]) <= 0:
                print('Inputted values are not in the range of integers 1 to 9.')
                print('This is not a Lo Shu magic square.')
                exit()

    # checking to see if all the row sums are the same
    if row_sums[0] == row_sums[1] == row_sums[2]:
        print('The rows all add to', row_sums[0])
    else:
        # program terminates if they are not the same
        print('This is not a Lo Shu magic square.')
        exit()

    # checking to see if all the column sums are the same
    if col_sums[0] == col_sums[1] == col_sums[2]:
        print('The columns all add to', col_sums[0])
    else:
        # program terminates if they are not the same
        print('This is not a Lo Shu magic square.')
        exit()

    # calculating the diagonal sums
    diagonal_sum1 = two_d_list[0][0] + two_d_list[1][1] + two_d_list[2][2]
    diagonal_sum2 = two_d_list[0][2] + two_d_list[1][1] + two_d_list[2][0]

    # checking to see if the diagonal sums are the same and equal to the row/column sums
    if diagonal_sum1 == diagonal_sum2 == row_sums[0]:
        print('The diagonals also all add to', diagonal_sum2)
    else:
        # program terminates if not
        print('This is not a Lo Shu magic square.')
        exit()

    # creating a set out of the 2d list elements contained in the 1d list. this is to check that all value are unique.
    uniqueness_check_set = set(conversion1d_list)

    # lengths should be the same if elements are all unique. this is the last step we have to verify, therefore we can
    # conclude if the inputted results are a magic square or not.
    if len(conversion1d_list) == len(uniqueness_check_set):
        print('The values are all unique.')
        print('This is a Lo Shu magic square.')
    else:
        # if not unique, program terminates
        print('The values are not all unique.')
        print('This is not a Lo Shu magic square.')
        exit()


main()


#######################################################################################################################

# 12. Prime Number Generation. User enters an integer. A list of prime numbers up to and including the integer is
# printed back to the user.

def main():
    # initializing the list of prime numbers
    prime_list = []
    print('This program will show all of the primes up to an inputted integer in a list.')
    # getting user integer
    users_int = int(input('Please enter an integer: '))
    # calling the integer list creation function to create a list of all the integers up to the inputted integer
    all_integers_list = integer_list_creation(users_int)

    # going through each element in the integer list
    for i in range(len(all_integers_list)):
        # running each element through the is_prime function to check if the element is prime
        prime_test_integer = all_integers_list[i]
        if is_prime(prime_test_integer) is True:
            # if the number is found to be prime, appends the element to the prime number list
            prime_list.append(prime_test_integer)
        else:
            # otherwise the loop continues to run
            pass
    # printing the list of primes to the user
    print('All the primes numbers up to an including your inputted integer', users_int, 'are as follows: ')
    print(prime_list)


# function to create a list of integers given an integer. list will include all integers up to and including the
# inputted integer

def integer_list_creation(integer):
    holding_list = []
    for i in range(1, integer + 1):
        holding_list.append(i)
    return holding_list


# function to check if the inputted integer is prime or not.
def is_prime(integer):
    if integer == 1:  # covering the case of 1 being passed. 1 is not a prime.
        return False
    elif integer <= 0:  # covering the case of negative numbers and 0 being inputted, which are all not prime.
        print('Negative numbers can\'t be prime!!')  # chastising the user for inputting a negative
        return False
    i = 2  # need to start the dividing value above 1, as n % 1 is always 0 and will return False.
    prime = True  # initialization at true
    # loop will increasingly go through integers 2 to n, and check if the argument is divisible
    while i < integer:
        if integer % i == 0:  # modulus
            prime = False  # changes value to false if the number is found to be divisible, and therefore not prime
            return prime  # ends the function and returns false
        else:
            i += 1  # accumulator to go through the integers
    return prime  # returns prime if the loop is exhausted, will mean prime is still true


main()
