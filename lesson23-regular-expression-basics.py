# To print the actual index position, use this
# phoneNumber = '6125986125'

# for i in phoneNumber:
#   print(phoneNumber.index(i))

# This prints the key value pair (enumerate is a built in method)
# for index, item in enumerate(phoneNumber):
#   print(index, item)


# regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing the last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))   

message = 'call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
foundNumber = False
# the chunk part of this for loop is slicing through the larger string in 12 character
# portions to look for a phone number
# writing it with [i:i+12] takes a 12 character slice of the string,
# going up by an index of one each time, eventually catching the phone number slices
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: %s' % chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')