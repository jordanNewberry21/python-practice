import re


# digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9|0)')

# /d = any numeric digit from 0 to 9
# /D = any character that is not a numeric digit from 0 to 9
# /w = any letter, numeric digit, or the underscore character
# /W = any character that is not a letter, numeric digit, or the underscore character
# /s = any space, tab, or newline character
# /S = any character that is not a space, tab, or newline

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 callings birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree.'''

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall(lyrics))


# make your own character classes

vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
# vowelRegex = re.compile(r'[a-z]')
# vowelRegex = re.compile(r'[A-F]')

print(vowelRegex.findall('Robocop eats baby food.'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') # looking for two vowels in a row


# Negative character classes
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
# the carrot (^) character turns this character class into a negative character
# this tells the computer to search for and match everything EXCEPT the character inside the brackets

