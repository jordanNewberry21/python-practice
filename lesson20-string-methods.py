# string methods return a new value rather than modifying in place
# this is because strings as a data type are immutable

spam = 'Hello world!'

print(spam.upper())

print(spam.lower())

answer = input()

if answer == 'yes':
    print('Playing again.')

answer.lower()

# lower() and upper() methods return the string as lower or uppercase, respectively
# a useful scenario for these methods could be making a case-insensitive comparison

# isupper() and islower() returns a boolean value
# methods are checking to see if there are upper or lower case values in a string

spam = 'Hello world!'
print(spam.islower()) # returns false because of the capital H

spam = 'HELLO WORLD!'
print(spam.isupper()) # returns true because all characters in the string are uppercase

spam = ''
print(spam.isupper())
print(spam.islower())
# both methods here return false because there needs to be one character
# of the method type to return true

# isalpha() -- checks if string is letters only
# isalnum() -- checks if string is letters and numbers only
# isdecimal() -- checks if string is numbers only
# isspace() -- checks if string is whitespace only
# istitle() -- titlecase only

