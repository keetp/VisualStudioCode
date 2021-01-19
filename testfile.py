def square_digits(num):
    new_str = ""
    for dig in str(num):
        new_str += str(int(dig)**2)
    return new_str
print(square_digits(52))