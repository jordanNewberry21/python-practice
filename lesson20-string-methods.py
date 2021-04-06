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

# startswith() -- checks if string starts with whatever argument is passed in
# endswith() -- checks if string ends with whatever argument is passed in

print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

print('My name is Simon'.split())

# rjust() and ljust() methods will return a padded version of a string
print('Hello'.rjust(10))
# the first argument is an integer that is telling the method how many spaces
# of padding to add to the string, on the right or left side as specified

print('Hello'.rjust(20, '@'))
# the second argument is a 'fill character' where instead of white space
# it adds in whatever character is specified, this can only be one character long

print('Hello'.center(20, '%'))
# center() does the same thing as rjust and ljust but center aligns it

spam = 'Hello'.center(20)

print(spam)
print(spam.strip())

# strip() removes characters from a string
# it's default behavior is to remove white spaces
# but any characters can be passed in as an argument
# and strip() will look through the string from the beginning and end
# until no matching characters are found
# there are also lstrip() and rstrip() methods to strip away from one side of the string


spam = 'Hello there.'
print(spam.replace('e', 'XYZ'))

