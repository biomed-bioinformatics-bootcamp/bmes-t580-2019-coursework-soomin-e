print('---------------------------------')
print('      Guess The Number App       ')
print('---------------------------------')

#User Name
name = input('What is your name? ')


# Library Imports
import random

# Generate Random Number
randomNum = random.randint(0,100)
guess = -1

# Guessing the Number
while guess != randomNum:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < randomNum:
        print('Sorry', name, 'your guess of', guess, 'is too low.')
    elif guess > randomNum:
        print('Sorry', name, 'your guess of', guess, 'is too high.')
    else:
        print('Excellent work {}, you won! It was {}!'.format(name, guess))
        

