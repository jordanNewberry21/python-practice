import os

totalSize = 0
for filename in os.listdir('/Users/jordannewberry/Prime/Week-10-Lecture-Stuff/'): # directory path to be examined
    if not os.path.isfile(os.path.join('/Users/jordannewberry/Prime/Week-10-Lecture-Stuff/', filename)):
        print('it exists.')
    else: 
        print('it doesnt exist')