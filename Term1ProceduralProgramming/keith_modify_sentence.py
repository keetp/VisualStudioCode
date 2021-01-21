# user inputs a sentence. the program performs three modifications to the sentence and prints them to the user

def main():
    # alerting user to what's going on
    print('This program will modify an inputted sentence in three different ways.')
    # asking user to input a sentence
    user_sentence = input('Please enter a full sentence: ')
    # printing the user's sentence back to them
    print('This is your sentence: ')
    print(user_sentence)
    # printing modified sentences to user
    print('Here are the modified sentences: ')
    # printing the sentence in all uppercase letters
    print(user_sentence.upper())
    # printing the sentence in all lowercase letters
    print(user_sentence.lower())
    # printing the sentence with all lowercase t's replaced with uppercase T's
    print(user_sentence.replace('t', 'T'))


main()
