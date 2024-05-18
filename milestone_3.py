import random

word_list = ['grapes', 'plum', 'strawberries', 'melon', 'apple']
word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input('Enter a letter: ').lower()

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please enter a single alphabetical letter.')

    

    def check_guess(guess):
        if guess in word:
            print(f'Good Guess!! {guess} is in the word.')
        else:
            print(f'Try again, {guess} is not in the word')
    
    return check_guess(guess)

ask_for_input()