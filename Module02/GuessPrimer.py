print('---------------------------------')
print('        Guess The Primer         ')
print('---------------------------------')

#User Name
name = input('What is your name? ')

# Library Imports
import random

# Generate Random Number
goal = random.choice('ATCG')
goal += random.choice('ATCG')
goal += random.choice('ATCG')
goal += random.choice('ATCG')
goal += random.choice('ATCG')
goal += random.choice('ATCG')
goal += random.choice('ATCG')

guess = 'NNNNNN'

# Guessing the Number
while guess != goal:
    guess = input('Guess a 6 based pair primer: ')

    misses = 0

    for i in range(len(guess)):
        if guess[i] != goal[i]:
            misses += 1

# Results depending on the guess
    if guess != goal:
        print('Sorry %s your guess of %s has %i base pairs wrong. Play again.' % (name, guess, misses))
    else:
        print('Excellent work {}, you won! It was {}!'.format(name, guess))