# 1. Assigning y to 20 and z to 40 if x is greater than 100.
x = 0
if x > 100:
    y = 20
    z = 40

# 2. Assigning b to 0 and c to 1 if a is less than 10.
a = 0
if a < 10:
    b = 0
    c = 1

# 3. Assigning b to 0 if a is less than 10, otherwise assign 99 to b.
a = 0
if a < 10:
    b = 0
else:
    b = 99

# 4. Rewriting the if-else statements.
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is D.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

# 5. Prints the greater of amount1 and amount2 granted amount1 is greater than 10 and amount2 is less than 100:
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    if amount2 > amount1:
        print(amount2)
    if amount1 == amount2:
        print('Both values are the equal.')

# 6. Determining if the speed is between 24 and 56.
if 24 < speed < 56:
    print('Speed is normal.')
else:
    print('Speed is abnormal')
