helloFile = open('/Users/jordannewberry/Desktop/helloFile.txt', 'w')

helloFile.write('Hello!!!!!!!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!!!!!!!\n')

helloFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

# to open a file it must always be saved into a variable like so
baconFile = open('bacon.txt', 'a') 
# this 'a' as a second argument is signaling to the OS to open this file in APPEND mode
# append mode simply adds whatever you are writing onto the end of the file.

baconFile.write('\n\nBacon is delicious.')

baconFile.close()

import shelve
# the shelve module can store Python values in a binary file
shelfFile = shelve.open('mydata')

shelfFile['cats'] = ['Zophie', 'Pooka', 'Henry', 'Daisy']

print(shelfFile['cats'])

print(list(shelfFile.keys()))

print(list(shelfFile.values()))

shelfFile.close()