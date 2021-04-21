# Regex Dot-Star, and the Caret/Dollar Characters


import re

beginsWithHelloRegex = re.compile(r'^Hello')
# the caret(^) at the beginning of the line says this pattern must come at the BEGINNING of the string
mo = beginsWithHelloRegex.search('Hello there!')

print(mo)

endsWithWorldRegex = re.compile(r'world!$')
# the dollar sign ($) at the end of the pattern says this must come at the END of the string being searched
mo = endsWithWorldRegex.search('Hello world!')

print(mo)

allDigitsRegex = re.compile(r'^\d+\w\d+$')
# if you put the caret at the beginning
# and the dollar sign at the end of the regex pattern
# this tells the computer that the entire string must match the pattern
mo = allDigitsRegex.search('7326542645127x63546725467125')

print(mo.group())

atRegex = re.compile(r'.{1,2}at')

print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# the DOT/STAR syntax
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

print(nameRegex.findall('First Name: Jordan Last Name: Newberry'))
# DOT/STAR syntax is always in greedy mode by default
# use the ? mark syntax after the DOT/STAR to use non-greedy matching

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')

print(nongreedy.findall(serve))

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'

dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)

print(mo.group())


vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
# this second argument can also be shorthanded to re.I

