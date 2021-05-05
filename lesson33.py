# deleting files

import os
import shutil
import send2trash

# os.unlink('/Users/jordannewberry/Prime/job_hunt_backup/bacon.txt')
# os.unlink('/Users/jordannewberry/Prime/job_hunt_backup/JordanNewberry_CoverLetter.pdf')
# os.unlink('/Users/jordannewberry/Prime/job_hunt_backup/Jordan_Newberry_Resume.pdf')
# unlink deletes a single file

# os.rmdir('/Users/jordannewberry/Prime/job_hunt_backup')
# command used to delete a directory
# only works on empty directories

# shutil.rmtree('/Users/jordannewberry/Prime/job_hunt_backup')

# when doing these file delete functions
# it's best to always do a dry run first, since deleted files or folders can't be recovered

# the send2trash module is a 3rd party module that does exactly what it says

send2trash.send2trash('/Users/jordannewberry/Desktop/helloFile.txt') # this line doesn't work
