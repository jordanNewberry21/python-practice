import re
# re is a regex module for python

message = 'call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# the re.compile method is being used to format the regex
# then it is being saved to a variable
# the above line is a regex formatting for a phone number
# the \d is a regex character that represents a digit
mo = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))
# mo stands for match object
print(mo.group())
print(mo)

# call the re.compile() function to create a regex object
# call regex objects search() method to create a match object
# call the match objects group() method to get the matched string