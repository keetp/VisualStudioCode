# 1. Descending Order. The program receives three floating point inputs from a user and lists them in descending order,
# from largest to smallest.

# habit building of declaring the main function despite no subfunctions
def main():
    user_number_1 = 0.0  # initializations of variables that will be used for user input
    user_number_2 = 0.0
    user_number_3 = 0.0

    # asking the user for three floating point inputs and assigning them to different variables
    user_number_1 = float(input('Please enter the first floating point number that you wish to arrange in size: '))
    user_number_2 = float(input('Please enter the second floating point number: '))
    user_number_3 = float(input('Please enter the third floating point number: '))

    # covering the first case where user_number_1 is the largest of the three.
    if user_number_1 >= user_number_3 and user_number_1 >= user_number_2:
        # if the second inputted number is larger than the third inputted number
        if user_number_2 >= user_number_3:
            # prints the three numbers in descending order
            print(user_number_1, user_number_2, user_number_3)
        # if the third inputted number is larger than the second inputted number
        elif user_number_3 >= user_number_2:
            # prints the three numbers in descending order
            print(user_number_1, user_number_3, user_number_2)

    # covering the second case where user_number_2 is the largest of the three.
    if user_number_2 >= user_number_3 and user_number_2 >= user_number_1:
        # if the third number is bigger than the first number
        if user_number_3 >= user_number_1:
            # prints the three numbers in descending order
            print(user_number_2, user_number_3, user_number_1)
        # if the first number is bigger than the third number
        elif user_number_1 >= user_number_3:
            # prints the three numbers in descending order
            print(user_number_2, user_number_1, user_number_3)

    # covering the third case where user_number_3 is the largest of the three.
    if user_number_3 >= user_number_1 and user_number_3 >= user_number_2:
        # if the first number is bigger than the second number
        if user_number_1 > user_number_2:
            # # prints the three numbers in descending order
            print(user_number_3, user_number_1, user_number_2)
        # if the second number is bigger than the first number
        elif user_number_2 >= user_number_1:
            # prints the three numbers in descending order
            print(user_number_3, user_number_2, user_number_1)


# calling main function
main()