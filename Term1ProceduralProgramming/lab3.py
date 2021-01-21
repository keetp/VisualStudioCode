# 1. Days of the week. Asks for input as a number and correlates the number with a day of the week.

day = int(input('Please enter a number between 1 and 7:'))  # asking for input between 1 and 7
if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
else:
    print('The value you entered is not valid.')  # if value entered is not between 1 and 7, returns error.

# 2.Areas of rectangles. Asks for length and width of two rectangles and prints the biggest area.

length1 = float(input('What is the length of the first rectangle?'))
width1 = float(input('What is the width of the first rectangle?'))
length2 = float(input('What is the length of the second rectangle?'))
width2 = float(input('What is the width of the second rectangle?'))

area1 = length1 * width1  # first area calculation
area2 = length2 * width2  # second area calculation

if area1 > area2:
    print('The first rectangle has the bigger area, measuring', area1, 'squared units.')

elif area2 > area1:
    print('The second rectangle has the bigger area, measuring', area2, 'squared units.')
else:
    print('Both rectangles are the same area, measuring', area1, 'squared units.')

# 3. Age Classifier. Asks user for age and prints if they're an infant, child, teenager or adult.
age = int(input('Please enter an age in years:'))

if age < 1:
    print('The person is an infant.')
elif 1 < age < 13:
    print('The person is a child.')
elif 13 <= age < 20:
    print('The person is a teenager.')
elif age >= 20:
    print('The person is an adult.')
else:
    print('Invalid entry.')

# 4. Roman numerals. Takes a number from 1 to 10 and converts it to Roman numeral.

number = int(input('Please enter a number between 1 and 10:'))  # asking for input
if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')

else:
    print('The value you entered is not valid.')  # if value is not between 1 and 10.

# 5. Mass and Weight. Asks for mass in kg and if the weight is above 500 or below 100, returns a statement.

mass = float(input('Please enter the mass of your objects in kilograms:'))  # asking for input
weight = mass * 9.8  # 9.8 for the acceleration of gravity.

if weight > 500:
    print('This object is too heavy.')
elif weight < 100:
    print('This object is too light.')
else:
    print('The value you entered is not valid.')

# 6. Magic dates. Asks user for a date input and determines if the days times the months is equal to the year.


day = int(input('Please enter the day:'))  # all the inputs set as integers. floats break the program.
month = int(input('Please enter the month:'))
year = int(input('Please enter the last two digits of the year:'))

if month * day == year:
    print('The date is magic.')
else:
    print('The date is not magic. :(')

# 7 Color Mixer. Gives out primary color combinations. Takes into account that the user could enter two colors in
# different orders.
color1 = str(input('Please enter the name of the first primary color:'))
color2 = str(input('Please enter the name of the second primary color:'))

if color1 == "red" and color2 == "blue":
    print('The secondary color is purple.')
elif color1 == "red" and color2 == "yellow":
    print('The secondary color is orange.')
elif color1 == "blue" and color2 == "red":
    print('The secondary color is purple.')
elif color1 == "blue" and color2 == "yellow":
    print('The secondary color is green.')
elif color1 == "yellow" and color2 == "red":
    print('The secondary color is orange.')
elif color1 == "yellow" and color2 == "blue":
    print('The secondary color is green.')
elif color1 == "yellow" and color2 == "yellow":
    print('You entered the same primary color twice.')  # covering user entering same color
elif color1 == "blue" and color2 == "blue":  # twice.
    print('You entered the same primary color twice.')
elif color1 == "red" and color2 == "red":
    print('You entered the same primary color twice.')
else:
    print('The initial colors you entered are not valid.')

# 9. Roulette wheel. A user enters a roulette pocket number and gets the color of the pocket back.

number = int(input('What number pocket do you wish to know the color of?'))

if number == 0:
    print('Green')
elif 0 < number < 11:
    if number % 2 == 0:  # using modulus to determine if the number is even/odd.
        print('Black')
    else:
        print('Red')
elif 11 <= number < 19:
    if number % 2 == 0:
        print('Red')
    else:
        print('Black')
elif 19 <= number < 29:
    if number % 2 == 0:
        print('Black')
    else:
        print('Red')
elif 29 <= number < 37:
    if number % 2 == 0:
        print('Red')
    else:
        print('Black')
else:
    print('Number does not exist on a roulette wheel')

# 11. Book Club Points. Gets user to enter how many books were purchased and returns how many points were accumulated.

books = int(input('How many books have you purchased this month?'))

if books == 0 or books == 1:
    print('You have earned 0 points.')
elif books == 2 or books == 3:
    print('You have earned 5 points.')
elif books == 4 or books == 5:
    print('You have earned 15 points.')
elif books == 6 or books == 7:
    print('You have earned 30 points.')
elif books >= 8:
    print('You have earned 60 points.')
else:
    print('There was an error.')

# 12. Software Sales. Shows user discount depending on how many packages were purchased.
packagePrice = 99  # constant is used a lot, avoiding magic numbers.
packagesBought = int(input('How many packages have you purchased?'))

if 0 < packagesBought < 10:
    print('You have no discount. Your purchase amount is', packagesBought * packagePrice)
elif 10 <= packagesBought < 20:
    print('Your discount is 10%. Your total is ', packagePrice * packagesBought * 0.9)
elif 20 <= packagesBought < 50:
    print('Your discount is 20%. Your total is ', packagePrice * packagesBought * 0.8)
elif 50 <= packagesBought < 100:
    print('Your discount is 30%. Your total is ', packagePrice * packagesBought * 0.7)
else:
    print('Your discount is 40%. Your total is ', packagePrice * packagesBought * 0.6)

# 13. Shipping Charges. Gets a weight of a package from a user and determines its shipping charges.

weight = float(input('Please enter the weight of your package in pounds.'))
# all rounded to two decimal places
if weight <= 2:
    print('The shipping cost for your package is $', round(weight * 1.50, 2))  # 1.5 is rate per pound
elif 2 < weight <= 6:
    print('The shipping cost for your package is $', round(weight * 3.00, 2))  # 3 is rate per pound.
elif 6 < weight <= 10:
    print('The shipping cost for your package is $', round(weight * 4.00, 2))  # 4 is rate per pound.
elif weight > 10:
    print('The shipping cost for your package is $', round(weight * 4.75, 2))  # 4.75 is rate per pound.

else:
    print('This value is not valid.')

# 16. February Days. User enters a year and the output tells if the year is a leap year.

year = int(input('Enter a year:'))

if year % 100 == 0:
    if year % 400 == 0:
        print('In', year, 'February has 29 days.')
    else:
        print('In', year, 'February has 28 days.')

elif year % 4 == 0:
    print('In', year, 'February has 29 days.')
else:
    print('In', year, 'February has 28 days.')
