# copying and moving files and folders

import shutil
# shutil stands for "shell utility" and it is a Python module for copying and moving files and folders

shutil.copy('/Users/jordannewberry/Prime/Week-10-Lecture-Stuff/python-practice/bacon.txt', '/Users/jordannewberry/Desktop')
# copy method takes first argument which is a file or directory, and copies it to whatever directory is specified in the second argument

shutil.copy('/Users/jordannewberry/Prime/Week-10-Lecture-Stuff/python-practice/bacon.txt', '/Users/jordannewberry/Desktop/baconCopyFile.txt')
# you can also specify a new name for the file by simply typing it into the second argument
# this will over write the original files name when it copies it

# shutil.copytree('/Users/jordannewberry/Desktop/job_hunt', '/Users/jordannewberry/Prime/job_hunt_backup')
# copytree copies and moves an entire directory at once
# use the second argument to specify the new file path at which to find the directory

shutil.move('/Users/jordannewberry/Prime/Week-10-Lecture-Stuff/python-practice/bacon.txt', '/Users/jordannewberry/Prime/job_hunt_backup')
# the .move() method works in the same way as .copy(), except it moves the original instead of making a copy

