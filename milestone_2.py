import random

favorite_fruit_list = ['melon', 'strawberries', 'grapes', 'plum', 'mango']

random_fruit = random.choice(favourite_fruit_list)

letter_input = input('Enter a single letter: ')

if len(letter_input) == 1 and letter_input.isalpha():
    print('Good Guess!!!')
else:
    print('Oops!! This is invalid!')