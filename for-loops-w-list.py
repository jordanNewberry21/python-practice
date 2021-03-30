supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# for loop shortcut
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


#  multiple assignments
cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
size, color, disposition = 'skinny', 'black', 'quiet'

a = 'AAA'
b = 'BBB'

a, b = b, a

# augmented assignment operators
spam = 42
spam = spam + 1
spam += 1
