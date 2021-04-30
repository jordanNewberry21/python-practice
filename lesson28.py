# regex sub() method and verbose mode

import re

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))


phoneRegex = re.compile(r'''
(\d\d\d-)|   # area code (without parens, with dash)
(\(\d\d\d\) )      # -or- area code with parens and no dash
(\d\d\d)   # it's kinda crazy that this works
-       # with VERBOSE mode you can format regex like this
        # and add comments like so
(\d\d\d\d)
\sx\d{2,4}   # ph. extension, like x1234 ''', re.VERBOSE | re.IGNORECASE | re.DOTALL)

print(phoneRegex.findall("(615) 456-3055 x123 sup dude how are you doing today"))




