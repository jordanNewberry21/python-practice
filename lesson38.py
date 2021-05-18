#!/usr/bin/env python3

# The WebBrowser Module

import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    # this line above is the join method and a slice to turn the system arguments, 
    # or CLI arguments into a string to be used as an address
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

