# # 1.
# if choice.upper() == 'Y':
#
# # 2.
# space_counter = 0
# for i in mystring:
#     if i == ' ':
#         space_counter += 1
#
# # 3.
# string_counter = 0
# for i in mystring:
#     if i.isdigit():
#         string_counter += 1
#
# # 4.
# string_counter = 0
# for i in mystring:
#     if i == i.lower():
#         string_counter += 1
#
# # 5.
#
# def end_check(string):
#     if string.endswith('.com'):
#         return True
#     else:
#         return False
#
# # 6.
#
# mystring = mystring.replace('t', 'T')
#
# # 7.
#
# def reverse_string(string):
#     reversestring = string[::-1]
#     print(reversestring)
#
# # 8.
#
# print(mystring[0:3])
#
# # 9.
#
# print(mystring[-3:])
#
# # 10.
#
# mystring = 'cookies>milk>fudge>cake>ice cream'
# appending_string = ''
# string_list = []
# for i in mystring:
#     appending_string += i
#     if i == '>':
#         appending_string = appending_string.strip('>')
#         string_list.append(appending_string)
#         appending_string = ''
# string_list.append(appending_string)
#
# print(string_list)