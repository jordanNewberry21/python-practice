# Walking a directory tree

import os

for folderName, subFolders, fileNames in os.walk('/Users/jordannewberry/Desktop/delicious'):
    print('The folder is', folderName)
    print('The subFolders in', folderName, 'are:', str(subFolders))
    print('The fileNames in', folderName, 'are:', str(fileNames))
    print()

# this is the general setup for using the os.walk() method
# here it is used in a for loop with 3 values being returned each iteration
# these 3 values are TACOS, you can call them whatever you want