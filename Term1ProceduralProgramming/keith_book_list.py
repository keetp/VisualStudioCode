# a student is selling used textbooks. program asks for each book price, assigns to a list and calculates the total
# cost of the books.

def main():
    # initializing list of textbook prices
    price_list = []
    # initializing total price of textbooks
    total_price = 0
    # asking user prices of individual textbooks and assigning to a variable
    report_writing_price = float(input('How much is the Report Writing textbook? '))
    system_analysis_price = float(input('How much is the Systems Analysis textbook? '))
    object_oriented_price = float(input('How much is the Object Oriented Programming textbook? '))
    database_price = float(input('How much is the Database Design textbook? '))
    # setting up the price list with the inputted price values
    price_list = [report_writing_price, system_analysis_price, object_oriented_price, database_price]

    # for each element in the price list
    for i in range(len(price_list)):
        # setting the current element to a variable
        current_text_price = price_list[i]
        # adding the text price to the running total of book prices
        total_price += current_text_price
    # printing to user the total amount of text book prices, formatting to two decimal places
    print('The total price of your textbooks is', '$' + format(total_price, '.2f'))

main()
