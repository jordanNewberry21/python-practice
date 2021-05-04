# filenames and absolute/relative file paths

import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

print(os.getcwd())

print(os.chdir(r'/Users/jordannewberry/'))

print(os.getcwd())

#  two kinds of file paths: ABSOLUTE and RELATIVE paths
# ABSOLUTE paths show the entire path of the file down to the root directory
# RELATIVE paths refer to path of the file in relation to the current working directory

# the . and the .. folders
# one dot (.) means "this directory"
# two dots (..) means "the parent of this directory"

os.path.abspath('spam.png')

os.path.abspath(r'../../spam.png')

os.path.isabs(r'../../spam.png') # returns false

os.path.isabs(r'../../spam.png') # returns false

os.path.relpath(r'../../spam.png', r'c:\folder1')

os.path.dirname('/Users/jordannewberry/') # pass in file to get directory name

os.path.basename('/Users/jordannewberry/') # pass in file path to pull out the base file name or folder

os.path.exists('/Users/jordannewberry/') # pass in file path, will return true if file exists, or false if it doesn't exist

os.path.isfile('/Users/jordannewberry/') # pass in file path, will return true if the path is a file, false if anything else

os.path.isdir('/Users/jordannewberry/') # pass in file path, will return true if path is a directory, false if file

os.path.getsize('/Users/jordannewberry/') # pass in file path, will return the size of the file / dir in bytes

os.listdir('/Users/jordannewberry/') # pass in directory path, will return a list of all the file names inside the directory

