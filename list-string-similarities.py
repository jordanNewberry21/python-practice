# lists are a mutable data type
# strings are not a mutable data type

# create a new string using slices
name = 'Zophie a Cat'

# slices can be used to modify strings even though they are immutable
newName = name[0:7] + 'the' + name[8:12]

print(newName)
# lists and other mutable objects when assigned to variables are given a reference # by python
# references
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

# list references
spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
# in this example, cheese is assigned to spam,
# which copies the reference to the cheese variable
# this creates a situation where when you update the cheese variable,
# the spam will be updated too because they share the exact same reference
print(cheese)

print(spam)

# MUTABLE OBJECTS SUCH AS LISTS ARE GIVEN REFERENCES, DO NOT FORGET THIS


# line continuation concepts
spam = ['apples',
        'oranges',
        'bananas',
        'cats']

# the backslash "\" tells python you need to move to a new line
# and it will ignore the indentation
print('Four score and seven ' + \
    'years ago')

