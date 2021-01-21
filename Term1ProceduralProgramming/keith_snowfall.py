# 2. Snowfall. User enters the amount of snowfall each day for a 7 day period. Program prints how much fell on each day
# and the total snowfall for the entire week period. Probably not the way this was intended to be done but I couldn't
# figure out how to return the day names along with the inputs after the loop finished.

def main():
    # initializing the variable we will be holding the total amount of snow throughout the week in
    snowfall_accumulator = 0
    # initializing the variable that the user input from day to day will be held in
    snowfall_daily = 0

    # alerting user that the program has started, along with instructions
    print('The following program will ask you to enter the amount of snow that has fallen on a particular'
          ' day of the week. All snowfall values are in centimeters.')
    # iterating a loop for each day of the week
    for i in range(1, 8):
        # calling function to convert the day number into the name of the day.
        day_name = day_number_to_day_name(i)
        # asking user for how much snow fell on a particular day
        print('How much snow fell on', day_name)
        snowfall_daily = float(input())
        # reading back what the user has enter to the user. couldn't figure out how to return it after all the inputs
        # were inputted and have it show the names of the days properly
        print('Snowfall on ', day_name, snowfall_daily, 'cm')
        # accumulator increases with each user input
        snowfall_accumulator += snowfall_daily

    # telling the user how much snow fell over the course of a week.
    print('The total amount of snow that fell over the course of the week was', snowfall_accumulator, 'cm')


# function to associate a name of a day of the week with a number, starting at Sunday. used for ease of printing
# within the for-loop. 1 = sunday, 2 = monday, etc until 7 = saturday.
def day_number_to_day_name(dayNumber):
    if dayNumber == 1:
        return 'Sunday: '
    elif dayNumber == 2:
        return 'Monday: '
    elif dayNumber == 3:
        return 'Tuesday: '
    elif dayNumber == 4:
        return 'Wednesday: '
    elif dayNumber == 5:
        return 'Thursday: '
    elif dayNumber == 6:
        return 'Friday: '
    elif dayNumber == 7:
        return 'Saturday: '


# calling main function
main()
