# 3. Tickets. There are four levels of seating at a concert, each having different costs. The user enters how many
# tickets of each level were bought and the program prints the total price and the price associated with each level
# of seating

def main():
    # asking user how many of each ticket level were purchased

    tickets_purchased_level_1 = int(input('How many level 1 tickets were purchased? '))
    tickets_purchased_level_2 = int(input('How many level 2 tickets were purchased? '))
    tickets_purchased_level_3 = int(input('How many level 3 tickets were purchased? '))
    tickets_purchased_level_4 = int(input('How many level 4 tickets were purchased? '))

    # calling each individual pricing function to calculate how much was spent on each particular level of seating.
    level_1_total = ticket_level_1(tickets_purchased_level_1)
    level_2_total = ticket_level_2(tickets_purchased_level_2)
    level_3_total = ticket_level_3(tickets_purchased_level_3)
    level_4_total = ticket_level_4(tickets_purchased_level_4)
    # calculating the grand total of the tickets purchased by adding all the individual totals.
    grand_total = level_1_total + level_2_total + level_3_total + level_4_total

    # printing to the user how much was spent on each particular ticket level.
    print('You purchased', tickets_purchased_level_1, 'level 1 tickets, totalling $'
          , format(level_1_total, '.2f'))
    print('You purchased', tickets_purchased_level_2, 'level 2 tickets, totalling $'
          , format(level_2_total, '.2f'))
    print('You purchased', tickets_purchased_level_3, 'level 3 tickets, totalling $'
          , format(level_3_total, '.2f'))
    print('You purchased', tickets_purchased_level_4, 'level 2 tickets, totalling $'
          , format(level_4_total, '.2f'))
    # and printing the grand total of the purchase for all the tickets to the user
    print('The grand total of your purchase is $', format(grand_total, '.2f'))


# function for level 1 ticket pricing, taking amount of tickets as an input.
def ticket_level_1(number_tickets):
    ticket_price = 290
    total = number_tickets * ticket_price
    return total

# function for level 2 ticket pricing, taking amount of tickets as an input.
def ticket_level_2(number_tickets):
    ticket_price = 220
    total = number_tickets * ticket_price
    return total

# function for level 3 ticket pricing, taking amount of tickets as an input.
def ticket_level_3(number_tickets):
    ticket_price = 180
    total = number_tickets * ticket_price
    return total

# function for level 4 ticket pricing, taking amount of tickets as an input.
def ticket_level_4(number_tickets):
    ticket_price = 90
    total = number_tickets * ticket_price
    return total

# calling main function
main()
