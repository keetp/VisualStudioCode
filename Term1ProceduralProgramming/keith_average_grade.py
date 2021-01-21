# program that opens the file grades.txt, reads the contents and prints the average of the grades contained on the file

def main():
    try:
        # opening the grades.txt file in read mode
        infile = open('grades.txt', 'r')
        # initializing sum of grades
        sum_of_grades = 0
        # initializing the number of lines
        number_of_lines = 0
        # reading through each line in the file
        for line in infile:
            # telling the compiler that the current line is a number
            number_on_line = float(line)
            # adding the current line to the running total of grades
            sum_of_grades += number_on_line
            # accumulating the number of lines in the file
            number_of_lines += 1
        # closing the file
        infile.close()
        # calculating the average
        average_grade = sum_of_grades / number_of_lines
        # printing average to the user
        print('The average of the grades found on the inputted file is', format(average_grade, '.2f'))
    # if an IOError is raised, prints an error to the user
    except IOError:
        print('ERROR: File could not be properly read. Please check that the file is in the proper directory.')
    # if a ValueError is raised, prints an error to the user
    except ValueError:
        print('ERROR: Program has attempted to read a non-number as a number. ')


main()