# import random

# print(random.randint(1, 10))

# import sys
# print('Hello')
# sys.exit()
# print('Goodbye')

# import pyperclip
# pyperclip.copy('Hello World!')

# print(pyperclip.paste())


# def hello(name):
#     print('Howdy!' + name)
#     print('Howdy!!!' + name)
#     print('Hello there.' + name)

# hello('Bob')
# hello('Jordan')
# hello('Cassen')

# def plusOne(number):
#     return number + 1

# newNumber = plusOne(5)
# print(newNumber)

# def spam():
#     global eggs
#     eggs = 'Hello'
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)

# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except:
#         print('Error: You tried to divide by zero.')

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

# print('How many cats do you have?')
# numCats = input()
# try:
#     if int(numCats) >= 4:
#         print('That is a lot of cats')
#     elif int(numCats) < 0:
#         print('Please enter a positive integer')
#     else:
#         print('That is not that many cats.')
# except:
#     print('You did not enter a number.')

# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20!')
secretNumber = random.randint(1 ,20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this is the correct guess!!

if guess == secretNumber:
    print('Good job, ' + name+ '! You guess my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber) + '.')


print('You took ' + str(guessesTaken) + ' guesses.')

