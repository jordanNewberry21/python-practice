# dictionaries are lists of many values
# they can contain all sorts of data types

# dictionaries are unordered by nature

myCat = {'size': 'fat', 'color': 'blue', 'disposition': 'loud'}

print('my cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42: 'The Answer'}
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'name': 'Zophie', 'species': 'cat', 'age': 8}

# dictionaries can be compared and will return true even if
# not in the correct key:value pair

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

# Tuples are just like lists, but are immutable
# they use parentheses instead of square brackets

print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

# the GET method in python
# this method takes two arguments,
# first argument is the key of the value you are searching for
# second argument is the default return value if the key is not found
print(eggs.get('age', 0))

print(eggs.get('color', ''))

picnicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')

# opposite of the get method in python is the setdefault() method
eggs.setdefault('color', 'black')

print(eggs)
