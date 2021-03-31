# names refer to values; i.e. x = 23
# many names can refer to one value, i.e. x = 23, y = x, both refer to 23
# names are reassigned independantly
# values live until no references
# assignment never copies data
# changes are visible through all names that are referenced


# mutable aliasing
    # you need a mutable value
    # more than one name
    # the value changes


# immutable values can't alias
    # types: ints, floats, strings, tuples

# "Change" is unclear
# Changing an int: rebinding, i.e. x = x + 1
# Changing a list: mutating, i.e. nums.append(7)
# you can rebind lists too

# Mutable and immutable objects are assigned the same way
# assignment is the same for all values
# aliasing can make it seem different

# references can be more than just names
# list elements are references, for example

# lots of different things are references
    # object attributes
    # list elements
    # dictionary values (and keys!)
    # anything on the left side of an assignment


# additionally, lots of things are actually assignments
    # X = ...
    # for X in ...
    # class X(...):
    # def X(...):
    # def fn(X):
    # import X
    # from ... import X
    # except ... as X:
    # with ... as X:


# function arguments are assignments
# anything that is assigned a value inside the function goes away
# when the function finishes running
# best way to avoid mutable aliasing is to just return new values
# from the function instead of mutating old values


# python is dynamically typed
# any name can be any value at any time
# NAMES HAVE NO TYPE
# VALUES HAVE NO SCOPE
# Python is call-by-assignment

board = [[0] * 8] * 8
board = [[0] * 8 for _ in range(8)]