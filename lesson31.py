# reading and writing plainText files

# binary files are any other type of file other than a plainText file

plainTextFile = open('/Users/jordannewberry/Desktop/plainText1.txt', 'w')
# a second argument can be passed into this open() method
# you can enter in 'w' to tell the computer you want to open this file in write mode
# or you can enter in 'a' to tell the computer to want to open this file in append mode
# append mode will just add stuff on to the end of the file

# print(plainTextFile.read())

# content = plainTextFile.read()

# print(content)

print(plainTextFile.readlines()) # this will print out the files contents as a list of strings

plainTextFile.close()

