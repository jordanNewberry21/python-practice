# double quotes avoid messing up with apostraphes
str = "That is Alice's cat."

# escape characters
str2 = 'Say hi to Bob\'s mother!'

# backslash is used before certain characters to denote certain text things for example
#  \' = single quote in string
# \" = double quote in string
# \t = tab in string
# \n = new line in string
# \\ = backslash in string


print('Hello there!\nHow are you?\nI\'m fine.')

# raw strings don't treat backslashes as escape characters,
#  similar to the template literal in javascript
print(r'Hello')
print(r'That is carol\'s cat.')


# multi-line string
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely, 
Bob.""")


# in and not in  methods are case sensitive
# strings can being and end with double quotes
# escape characters let you put quotes and other characters that are hard to type into strings
# raw strings will literally print any backslashes in the string and ignore escape characters
# multiline strings begin and end with three quotes, and can span multiple lines.
# indexes, slices, and the in and not in operators all work with strings.