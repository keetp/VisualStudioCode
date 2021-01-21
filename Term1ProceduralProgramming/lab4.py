#### Keith Rogers, Procedural Programming lab 4 ####
#### Tuesday, Oct 13th, 2020                    ####

import turtle  # importing turtle library for later use.

# 1. Bug Collector. A collector collects bugs every day for 5 days. The program tracks and keeps a running total
# of the total bugs he collects for every day of the 5.

TotalBugs = 0  # initializing

for x in range(1, 6):  # need to start at 1 and end at 6 to print the day value correctly
    print('Value for Day', x)  # keeping track of which day the input is on
    TotalBugs += int(input('How many bugs have you collected today?'))

print('You have collected', TotalBugs, 'bugs in total.')

# 2. Calories Burned. Displays the amount of calories burned at different predetermined minute values.

calories = 4.2  # calories per minute

for x in [10, 15, 20, 25, 30]:  # different minute values that calories burned are calculated at
    print('It has been', x, 'minutes; you have burned', calories * x, 'calories')

# 3. Budget Analysis. User inputs a budget, then inputs separate expenses. Program tells the user if they are over
# or under budget

budget = 0  # initializations
NetBudget = 0
MorePrompt = 'y'  # value for if user wants to enter more expenses.

UserExpenses = float(input('What is your total budget?'))

while MorePrompt == 'y':
    budget += float(input('Please enter expense:'))
    MorePrompt = str(input('Do you have another expense? (y to continue)'))  # user prompt

NetBudget = UserExpenses - budget  # the amount over/under budget

if budget <= UserExpenses:
    print('You are within budget!')
    print('You have a surplus of $', NetBudget)
else:
    print('You are over budget.')
    print('You have a deficit of $', NetBudget)

# 4. Distance Traveled. Asks user for speed of vehicle and time traveled, and prints speed at each hour.

speed = float(input('What is the speed of the vehicle?'))
time = int(input('How many hours have you been traveling?'))

print('Hour\t', 'Distance Traveled:')

for x in range(time):
    print(x + 1, '\t\t', (x + 1) * speed, 'km')  # x+1 since range starts at (time-1)

# 5. Average Rainfall. Calculates rainfall over the course of an inputted amount of years. Shows average rainfall,
# total amount of months and the total rainfall.

rainfall = 0  # initializations
months = 0
years = int(input('How many years?'))

for x in range(years):
    print('Year', x + 1)  # x+1 since range starts at x-1, for organizational purposes
    for i in range(1, 13):
        print('Month', i)  # prints which month for ease of use
        rainfall += int(input('How many inches of rain during this month?'))
        months += 1

print('Total of', months, 'months.')
print('The average rainfall per month is', round(rainfall / months, 2), 'inches')  # average inches per month
print('The total amount of rainfall is', rainfall, 'inches')

# 6. Celsius to Fahrenheit, Shows the celsius to fahrenheit conversion for 0-20 celsius.

print('Celsius\t\t', 'Fahrenheit')  # header for the table

for x in range(21):  # range to x-1 for 20 celsius
    print(x, '\t\t\t', round((9 / 5) * x + 32, 2))  # blank string for formatting purposes.

# 7. Pennies for pay. Calculating the salary of someone that gets paid a penny a day and double that each consecutive
# day.

penniesTotal = 0  # variable for the total pennies earned
penniesPer = 1  # variable for pennies earned per day
days = int(input('How many days have you worked?'))

for x in range(1, days + 1):  # start at 1 instead of 0
    penniesPer *= 2
    print('Day', x, "\t$", penniesPer / 100)
    penniesTotal += penniesPer

print('You have earned $', penniesTotal / 100, 'over the course of', days,
      'days.')  # divided by 100 to get dollar amount.

# 8. Sum of numbers. A user enters a series of numbers to be added. An entry of a negative number signals
# the end of the series

seriesInput = 0  # input variable
seriesValue = 0  # holding variable for the series total

while seriesInput >= 0:  # runs while positive
    seriesInput = float(input('Enter the next positive number in the series (negative to signal a stop):'))
    if seriesInput >= 0:  # to ensure the inputted negative number doesn't get appended to the series total.
        seriesValue += seriesInput

print('The sum of your series of numbers is:',
      seriesValue)

# 10. Tuition increase. Tuition is set to increase by 3 percent each year for 5 years. Projected tuition is printed.

tuition = 8000  # initial tuition cost
tuitionIncrease = 1.03  # percent that the tuition is increasing by

for x in range(1, 6):
    print('Year', x, ':')  # over the course of 5 years
    for i in range(1, 3):  # 2 semesters per year
        print('Semester', i, end=': ')
        tuition *= tuitionIncrease  # calculating the increase
        print(round(tuition, 2))

# 12. Factorial of a number. User enters a non-negative integer and the program returns the factorial of that number.

factorialBase = int(input('Enter a non-negative integer: '))
factorialCalc = 1  # initialized at 1 because we're multiplying.

if factorialBase < 0:  # validates the input is positive
    factorialBase = int(input('This is not a positive integer, please re-enter:'))

for x in range(1, factorialBase + 1):  # starts at 1, consecutively multiplies until the inputted integer.
    factorialCalc *= x

print('The factorial of', factorialBase, 'is', factorialCalc)

# 14. Nested loops to draw an upside down staircase containing all * characters.

# initializing values used in loop parameters

rowNumber = 0  # amount of characters being printed in the row
rowValue = 0  # value used in nested loop to print the *
staircaseSize = 7  # for ease of editing if you wish to make a bigger staircase

for rowNumber in range(staircaseSize, 0, -1):  # start at 7, decrease by 1.
    for rowValue in range(rowNumber, 0, -1):  # runs rowNumber amount of times for each iteration
        print('*', end='')  # prints * without starting a new line for each iteration
    print('')  # creates new line

# 15. Drawing a cone shape with # characters.

# initializing loop parameters.

currentRow = 0
currentColumn = 0
coneSize = 6  # for ease of editing if you wish to make a bigger cone

for currentRow in range(coneSize):
    print('#', end='')  # prints the first # without making new line
    for currentColumn in range(currentRow):
        print('', end=' ')  # appends a blank space without making a new line
    print('#')  # adds the final # character to the cone and creates new line

# 18. Hypnotic square pattern with turtle. First time using turtle, apologies if my formatting isn't proper. Pretty fun
# messing around with this!

squareSize = 50  # for ease of editing

# repeatedly creating bigger and bigger squares without lifting the turtle up, which creates a hypnotic pattern.

for x in range(squareSize):
    turtle.pendown()  # placing the turtle down to start drawing
    turtle.backward(x * 5)  # initially moves 5 pixels backwards, getting bigger and bigger as the loop runs
    turtle.right(90)  # 90 degree turns
