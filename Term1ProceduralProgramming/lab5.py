import random  # importing random library for later use.


# 1. Kilometer Converter. Asks user to input a distance in km, converts the input to miles and prints.

def main():
    miles = float(input('Enter a distance in kilometers you wish to convert to miles:'))
    print(miles, 'km is', km_to_miles(miles), 'miles')  # calling the function km_to_miles with user input to convert


# function to convert kilometers to miles.
def km_to_miles(kilometers):
    # constant to convert km to miles
    conversion = 0.6214
    return round(kilometers * conversion, 2)


# Calling main function
main()
#######################################################################################################################
# 2. Sales tax, function version. Takes a purchase amount from a user and prints the sales tax associated with the
# purchase along with the sale total.

COUNTRY_SALES_TAX = 0.025  # global constants for the sales taxes
STATE_SALES_TAX = 0.05


def main():
    # taking purchase amount from user and assigning to a variable
    purchase_total = float(input('How much is your purchase?'))
    # calling function with user input to calculate country/state tax and assigns to a variable
    country_tax_total = country_tax(purchase_total)
    state_tax_total = state_tax(purchase_total)

    print('Country sales tax: $', country_tax_total)  # print statements to display to user
    print('State sales tax: $', state_tax_total)
    print('Total sales tax: $', round(country_tax_total + state_tax_total, 2))
    print('The total of your purchase: $', state_tax_total + country_tax_total + purchase_total)


# calculates country tax value using global constant, returns value when called.
def country_tax(purchase):
    return round(purchase * COUNTRY_SALES_TAX, 2)


# calculates state tax value using global constant, returns value when called.
def state_tax(purchase):
    return round(purchase * STATE_SALES_TAX, 2)


# calling main function
main()
#######################################################################################################################
# 3. How much insurance? User enters the cost that a structure would take to replace, the program tells the user
# the minimum amount they should insure it for.

MINIMUM_AMOUNT = 0.8  # 80% is recommended minimum, global constant


def main():
    housePrice = float(input('How much would it cost to replace your structure?'))  # taking user input
    print('The minimum amount you should insure your structure for: $', insurance_calc(housePrice))  # function call


# function that calculates and returns minimum insurance that it is recommended, given a structure price.
def insurance_calc(price):
    return round(MINIMUM_AMOUNT * price, 2)


# calls main function
main()


#######################################################################################################################
# 4. Automobile Costs. User enters monthly costs for various car expenses, program shows total monthly costs and
# total annual costs. Making everything individual functions might have been a mistake. Let me know if you think
# it would be cleaner to combine some of the functions. :)

def main():
    print('When prompted, please enter the monthly expenses for your car.')  # prepares user to input info

    loan_expense = get_loan()  # next 6 functions prompt user to enter a monthly expense
    insurance_cost = get_insurance()
    gas_expense = get_gas()
    oil_expense = get_oil()
    tire_expense = get_tires()
    maintenance_expense = get_maintenance()

    # the following 2 function calls calculate total annual and monthly expenses
    annual_expenses = total_annual_cost(loan_expense, insurance_cost, gas_expense, oil_expense,
                                        tire_expense, maintenance_expense)
    monthly_expenses = total_monthly_cost(loan_expense, insurance_cost, gas_expense, oil_expense,
                                          tire_expense, maintenance_expense)

    print('Your total monthly costs is $', format(monthly_expenses, ',.2f'))  # prints monthly and annual expenses
    print('Your total annual costs is $', format(annual_expenses, ',.2f'))  # with two decimal places showing


# function to get and return monthly loan payment
def get_loan():
    loan = float(input('Loan Payment: '))
    return loan


# function to get and return monthly insurance payment
def get_insurance():
    insurance = float(input('Insurance Payment: '))
    return insurance


# function to get and return monthly gas payment
def get_gas():
    gas = float(input('Gas Costs: '))
    return gas


# function to get and return monthly oil payment
def get_oil():
    oil = float(input('Oil Costs: '))
    return oil


# function to get and return monthly tire payment
def get_tires():
    tires = float(input('Tire Cost: '))
    return tires


# function to get and return monthly maintenance payment
def get_maintenance():
    maintenance = float(input('Maintenance Costs: '))
    return maintenance


# calculates total monthly cost off 6 inputs
def total_monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    total_monthly_cost_calc = loan + insurance + gas + oil + tires + maintenance
    return total_monthly_cost_calc


# calculates total annual cost off 6 inputs
def total_annual_cost(loan, insurance, gas, oil, tires, maintenance):
    total_annual_cost_calc = (loan + insurance + gas + oil + tires + maintenance) * 12
    return total_annual_cost_calc


# calling main function
main()


#######################################################################################################################
# 7. Stadium Seating. Ticket prices vary based on the classification of the ticket. User enters how many of each ticket
# was sold, program tells the user how many tickets were sold total and the total income.

def main():
    # asking user how many of each ticket was sold.
    tickets_sold_a = int(input('How many Class A tickets were sold? '))
    tickets_sold_b = int(input('How many Class B tickets were sold? '))
    tickets_sold_c = int(input('How many Class C tickets were sold? '))

    income_a = class_a_pricing(tickets_sold_a)  # income from A class tickets
    income_b = class_b_pricing(tickets_sold_b)  # income from B class tickets
    income_c = class_c_pricing(tickets_sold_c)  # income from C class tickets
    total_income = total_ticket_income(income_a, income_b, income_c)  # total income
    # total tickets sold, uses the same operations as the income calculation so I reused the function.
    total_tickets = total_ticket_income(tickets_sold_a, tickets_sold_b, tickets_sold_c)
    # print statements associated with each calculated total. the end='$' is only there because there was a small gap
    # between the dollar sign and the number and it irritated me.
    print('There were', tickets_sold_a, 'A class tickets sold, earning $', end='$')
    print(income_c)
    print('There were', tickets_sold_b, 'B class tickets sold, earning $', end='$')
    print(income_b)
    print('There were', tickets_sold_c, 'C class tickets sold, earning $', end='$')
    print(income_c)
    print('There were', total_tickets, 'total tickets sold, earning ', end='$')
    print(total_income)


# function for calculating class A tickets. could be included in the main function but I think it looks nicer this way.
def class_a_pricing(sold):
    total = sold * 20
    return total


# function for calculating class B tickets.
def class_b_pricing(sold):
    total = sold * 15
    return total


# function for calculating class C tickets.
def class_c_pricing(sold):
    total = sold * 10
    return total


# function for calculating total income, which also lets us calculate total tickets sold handily enough.
def total_ticket_income(total_a, total_b, total_c):
    net_earned = total_a + total_b + total_c
    return net_earned


# calling main function
main()


#######################################################################################################################
# 10. Feet to inches. User enters a length in feet and the program returns the amount of inches in that many feet.

def main():
    # user input
    feet = int(input('Convert feet to inches. Enter the number of feet you wish convert: '))
    inches = feet_to_inches(feet)  # passing user input through the feet_to_inches function
    print('The number of inches in', feet, 'feet is', inches, 'inches')


# function which takes the number of feet as an argument and converts feet to inches. returns inches.
def feet_to_inches(feet):
    inches = feet * 12  # 12 inches in a foot
    return inches


# calling main function
main()


#######################################################################################################################
# 11. Math Quiz. Simple math quiz that gives the user two numbers between 1 and 999 to add. Returns right answer
# if user inputs the incorrect answer.

# not really necessary to define a main function as we aren't using any other functions, just doing it to develop
# the habit of defining main.
def main():
    # assigning two random numbers to two variables
    number1 = random.randrange(1, 999)
    number2 = random.randrange(1, 999)
    # aligning both numbers with an addition symbol
    print(' ', number1)
    print('+', number2)

    # user input request for the answer, assigns to variable for checking
    answer = int(input('  '))

    # checking if the answer is right or wrong and returning the appropriate message
    if answer == number1 + number2:
        print("That's correct! You have a big brain!")
    else:
        print('Nope! The correct answer is', number1 + number2)


# calling main function
main()


#######################################################################################################################
# 12. Maximum of Two Values. Prompts user to enter two integer and prints the bigger of the two.

def main():
    # prompting user to enter two integers and assigns them to variables
    int1 = int(input('Enter the first integer: '))
    int2 = int(input('Enter the second integer: '))
    # validating that the integers inputted are not the same. if they are, attempts to get new input from the user.
    while int1 == int2:
        print('You entered the same integer twice, please re-enter your integers.')
        int1 = int(input('Enter the first integer: '))
        int2 = int(input('Enter the second integer: '))
    # runs the max function with the user inputs
    max_num = max(int1, int2)
    print(max_num, 'is the bigger of the two.')  # prints bigger integer


# function which takes two integers and returns the bigger of the two.
def max(integer1, integer2):
    if integer1 > integer2:
        return integer1
    elif integer1 < integer2:
        return integer2


# calls main function
main()


#######################################################################################################################
# 15. Test Average and Grade. Program takes 5 inputted test scores, assigns them a letter grade and determines
# the average.

def main():
    # the five test scores, inputted by a user, assigned a variable each
    test_score1 = float(input('First test score? '))
    test_score2 = float(input('Second test score? '))
    test_score3 = float(input('Third test score? '))
    test_score4 = float(input('Fourth test score? '))
    test_score5 = float(input('Fifth test score? '))

    # using the calc_average function to calculate the 5 tests average and assigning to a variable
    average_score = calc_average(test_score1, test_score2, test_score3, test_score4, test_score5)
    # printing the test scores that were inputted, along with the associated letter grade determined by
    # the determine_grade function
    print('The first score', test_score1, 'is a letter grade of', determine_grade(test_score1))
    print('The second score', test_score2, 'is a letter grade of', determine_grade(test_score2))
    print('The third score', test_score3, 'is a letter grade of', determine_grade(test_score3))
    print('The fourth score', test_score4, 'is a letter grade of', determine_grade(test_score4))
    print('The fifth score', test_score5, 'is a letter grade of', determine_grade(test_score5))
    # printing the average score, and passing the average_score through determine_grade to give an associated
    # letter value for the average
    print('The average score of all 5 tests is', average_score)
    print('This is an average letter grade of', determine_grade(average_score))


# function which takes 5 tests scores and returns the average
def calc_average(score1, score2, score3, score4, score5):
    average_score = (score1 + score2 + score3 + score4 + score5) / 5
    return average_score


# function which assigns a letter grade to a passed number grade value
def determine_grade(test_score):
    if 90 <= test_score <= 100:
        return 'A'
    elif 80 <= test_score <= 89:
        return 'B'
    elif 70 <= test_score <= 79:
        return 'C'
    elif 60 <= test_score <= 69:
        return 'D'
    else:
        return 'F'


# calls main function
main()


#######################################################################################################################
# 16. Odd/Even Counter. Generates 100 random numbers and determines how many are even and how many are odd.

def main():
    # initializations
    even_count = 0  # counter for even numbers
    odd_count = 0  # counter for odd numbers

    for i in range(100):  # 100 iterations
        random_number = random.randint(1, 1000000000)  # random integer
        if random_number % 2 == 0:  # mod 2 = 0 means even
            even_count += 1  # even accumulator increases by 1
        if random_number % 2 == 1:  # mod 2 = 1 means odd
            odd_count += 1  # odd accumulator increases by 1

    print(even_count, 'of the 100 random numbers are even.')
    print(odd_count, 'of the 100 random numbers are odd.')


# calling main function
main()


#######################################################################################################################
# 17. Prime Numbers. User inputs an integer, program tells the user whether or not the integer is prime or not.


def main():
    integer = int(input('Enter an integer to see if it is prime: '))  # prompting user for integer input
    prime_check = is_prime(integer)  # running integer input through the prime_check function
    if prime_check is True:  # if returns true, the integer is a prime
        print('This integer is prime.')
    else:  # otherwise it is not
        print('This integer is not prime.')


# function which takes an integer argument and determines if the integer is prime or not. Super slow with higher primes,
# really interesting to run. Really shows the importance of run time complexity.
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


# calls main function
main()


#######################################################################################################################
# 18. Prime Number List. Lists all prime numbers from 1 - 100. Uses previously built is_prime function from #17.

def main():
    print('This program will show you all the prime numbers from 1 and 100:')
    for i in range(1, 101):  # iterating from 1-100
        if is_prime(i) is True:  # calling the function is_prime, which returns True if the number is prime
            print(i, end=' ')  # prints if the function determines i is prime.
        else:
            pass  # does nothing and continues to iterate if is_prime is anything but True.


# calls main function
main()


#######################################################################################################################
# 20. Random Number Guessing Game. Program which stores a random number in a variable and gets the user to
# continually guess what the number is until the input matches the random number. Gives too high/too low messages
# and tracks the amount of attempts.

# not necessary to define main, no functions being used outside of the main, again just developing habit
def main():
    random_number = random.randint(1, 100)  # variable for a random number between 1 and 100
    number_of_attempts = 1  # initializing the number of attempts at 1 since the first input is outside of the loop
    print('Can you guess my number? It is between 1 and 100.')
    user_guess = int(input())  # starting the game at user input

    while user_guess != random_number:  # runs while the input isn't equal to the random number
        if user_guess > random_number:  # high guess, prints that the guess was too high, prompts for new input
            print('Too high! Try again.')
            user_guess = int(input())
            number_of_attempts += 1  # accumulator to track the number of attempts
        elif user_guess < random_number:  # low guess, prints that the guess was too low, prompts for new input
            print('Too low! Try again')
            user_guess = int(input())
            number_of_attempts += 1  # accumulator to track number of attempts

    # the loop breaks when the input is equal to the hidden random number. Prints a congratulations, the hidden number,
    # and how many attempts it took the user to guess the number.

    print('You got it! The random number was', random_number, end='. ')
    print('It took you', number_of_attempts, 'attempt(s).')


# calling main function
main()


#######################################################################################################################

# 21. Rock, Paper, Scissors Game. Play a game of rock paper scissors against the computer. I feel as if there is a much
# more elegant solution to this. Maybe I'll revisit this problem as we progress through course material.

def main():
    valid_choice = False  # boolean value initialization to check input validity
    continue_game = True  # boolean value initialization to keep the game running in event of a tie.

    while continue_game is True:  # to keep the game running in the event of a tie
        computers_number = random.randint(1, 3)  # assigning the computer a random integer from 1 to 3

        # calls function to convert the integer into a rock, paper, scissor choice
        computers_choice = number_to_word(computers_number)

        users_choice = str(input('Rock, paper or scissors (all lowercase)?'))  # user chooses rock/paper/scissor

        while valid_choice is False:  # validating that the user inputted rock, paper or scissors.
            if users_choice == 'rock':
                valid_choice = True  # True breaks the while loop
            elif users_choice == 'paper':
                valid_choice = True
            elif users_choice == 'scissors':
                valid_choice = True
            else:
                # re-prompts input otherwise
                users_choice = str(input('Not a valid choice. Remember to put your choice in all lowercase.'))
                valid_choice = False

        print('The computer has chosen', computers_choice)  # computers choice revealed

        # giant block of if statements that compare the users choice against the computers choice and then determines,
        # based off the rules of rock paper scissors, who wins.
        if users_choice == computers_choice:  # case where user and computer choose the same
            print('Tie! Go again.')
            continue_game = True  # the only case where the game and loop continues
        if users_choice == 'rock':  # case where user picked rock
            if computers_choice == 'scissors':
                print('Rock smashes scissors! You win!')
                continue_game = False  # a game value of false will break the while loop and end the game
            elif computers_choice == 'paper':
                print('Paper smothers rock! You lose!')
                continue_game = False
        elif users_choice == 'scissors':  # case where user picked scissors
            if computers_choice == 'rock':
                print('Rock smashes scissors! You Lose!')
                continue_game = False
            elif computers_choice == 'paper':
                print('Scissors cuts paper! You win!')
                continue_game = False
        elif users_choice == 'paper':  # case where user picked paper
            if computers_choice == 'rock':
                print('Paper smothers rock! You win!')
                continue_game = False
            elif computers_choice == 'scissors':
                print('Scissors cuts paper! You lose!')
                continue_game = False


# function which converts the computers random 1 to 3 number to a rock, paper, scissors choice. felt cleaner to put
# in a function separate from the main.
def number_to_word(number):
    if number == 1:
        return 'rock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'scissors'


# calling main function
main()
#######################################################################################################################
