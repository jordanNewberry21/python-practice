import re

# the question mark character preceding the group (wo) tells
# the computer we are looking for a group that may show up 0 - 1 times
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
print(mo.group())
# the * or star character means match 0 or more

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
print(mo.group())
# the + or plus sign character means match 1 or more times

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

# if you are searching for matches to any of these special characters
# they can be "escaped" in the compile method using the backslash '\' character before the special character

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234, 555-4242, 212-555-0000')
print(mo.group())

haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('HaHaHaHaHaHaHaHaHa')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('656-456-3055')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('6564563055')
print(mo.group())
# the question mark has a second use in regular expressions
# when placed behind a pattern, it tells the system to use non-greedy matching
# which looks for an returns the smallest possible match, in this case the first 3 numbers



