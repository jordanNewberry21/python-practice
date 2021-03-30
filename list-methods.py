spam = ['hello', 'hi', 'howdy', 'heyas']

# index method returns index of given argument
spam.index('hello')

# if duplicates are present in the list, the index method will return the first
# found 

spam = ['cat', 'dog', 'bat']
spam.append('moose')

print(spam)

spam.insert(1, 'chicken')

print(spam)

# there are specific methods for each data type!!!

spam = ['cat', 'bat', 'rat', 'elephant']
# .remove() gets rid of the specific element, no matter where it is in the list
spam.remove('cat')

print(spam)

# del or delete statement removes an item from the list by its index
del spam[0]

# in a string with multiple variables of the same value, .remove() will only
# remove the first value found
spam = ['cat', 'bat', 'rat', 'elephant', 'cat', 'hat']
spam.remove('cat') # only removes the first cat

print(spam)

spam = [2, 5, 3.14, 1, -7]
# .sort() method sorts the list automatically
spam.sort()

print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)

spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)