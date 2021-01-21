# 1. While loop. User enters a number which is multiplied by 10. The loop does not terminate until a product greater
# than 100 is returned.

product = 0  # initializations

while product < 100:
    number = float(input('Please enter a number:'))
    product = number * 10

# 2. While loop that asks the user for two numbers and sums them. Then checks if the user wants to run the program
# again.

num1 = 0  # initializations
num2 = 0
repeat = 'y'

while repeat == 'y':
    num1 = float(input('What is the first number you wish to add?'))
    num2 = float(input('What is the second number you wish to add?'))
    added = float(num1 + num2)  # using added since sum is a function in python
    repeat = str(input('Do you wish to perform the operation again? (Enter y for yes)'))

print(added)  # print isn't necessary; for troubleshooting purposes.

# 3. For loop that shows the multiples of 10 up to 1000, starting at 0.

for x in range(101):  # 101 since range stops at n-1
    print(10 * x)

# 4. Takes a number from a user 10 times and adds them. Prints at each iteration.

IncreasingSum = 0  # initialization

for x in range(10):
    IncreasingSum += float(input('Please enter a number:'))
    print(IncreasingSum)  # will print each iteration of the sum

# 5. For loop that prints the series 1/30 + 2/29 + 3/28 .. + 30/1.

series = 0  # initializing
denominator = 30  # denominator value which will decrease by 1 for each iteration.

for x in range(30):
    series += float((x + 1) / denominator)
    denominator -= 1

print(series)  # unnecessary to print, just for troubleshooting purposes.

# 6. Augmented assignment operators in Python.

x += 1
x *= 2
x /= 10
x -= 100

# 7. Displays a 10x15 matrix that has all # characters.

for x in range(10):
    matrix = ''  # reinitializing for each iteration
    for i in range(15):
        matrix += str('#')  # appending a # character each iteration
    print(matrix)

# 8. Gets the user to input a nonzero, positive number, and then validates the input.

number = float(input('Please type a nonzero, positive number:'))

while number <= 0:
    print('This is not a valid number.')
    number = float(input('Please try again:'))  # will prompt the user to retry if the number is not valid

# 9. Gets the user to input a number between 1 and 100, and validates the input.

number = float(input('Please enter a number between 1 and 100:'))

while number > 100 or number < 0:
    print('This is not a valid number.')
    number = float(input('Please try again:'))  # will prompt the user to retry if the number is not valid
