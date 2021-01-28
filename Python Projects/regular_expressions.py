# lessons retrieved from automatetheboringstuff.com.
# Python practice with regular expressions.

import re 

# using \d as a placeholder for digits. finding phone numbers of form xxx-xxx-xxxx

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My phone number is 415-555-4242')    # mo standing for matched objects

print(mo)   # directly printing the matched object will return something verbose and not super user friendly
print('Phone number:', mo.group())  # group will return the matched number without the additional text

# regex can also be used with paratheses to create groups. imagine you take the above example but are
# only looking for area codes

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo.group1(1)    # 415
mo.group2(2)    # 555-4242

mo.group(0) # full phone number
mo.group()  # same thing

mo.groups() # note groups with an S, returns tuple ('415', '555-4242')

areaCode, mainNumber = mo.groups()

# areaCode = 415        # mainNumber = 555-4242

