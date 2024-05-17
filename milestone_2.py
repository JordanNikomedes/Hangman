import random

word_list = ['melon', 'strawberries', 'grapes', 'plum', 'mango']

word = random.choice(word_list)

guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good Guess!!!')
else:
    print('Oops!! This is invalid!')