def printedFrame(words, leftOrRight):
  longest = ""
  for i in words:
    if len(i) > len(longest):
      longest = i
  maxlength = len(longest) + 4
  print ("*"*maxlength)
  if leftOrRight == 'left':
    for word in words:
      spaces = len(longest)-len(word) + 1
      spaces_2 = " " * spaces 
      print (f"* {word}{spaces_2}*")
  elif leftOrRight == 'right':
    for word in words:
      spaces = len(longest)-len(word) + 1
      spaces_2 = " " * spaces 
      print (f"*{spaces_2}{word} *")
  else:
    for word in words:
      spaces = len(longest)-len(word)
      if spaces % 2 == 0:
        centerSpace = int(spaces / 2)
        blankSpace = " " * centerSpace
        print (f"* {blankSpace}{word}{blankSpace} *")
      else:
        centerSpace = int(spaces / 2)
        blankSpace = " " * centerSpace
        print (f"* {blankSpace}{word}{blankSpace}  *")
  print ("*"*maxlength)

leftOrRight = input('''Would you like this left or right aligned? Enter 'left' or 'right'.\n''')

words = ["Helldbds;agsberougbawo", "YAYAYAYAYAYAYAYA", "in", "a", "frame"]
printedFrame(words, leftOrRight)