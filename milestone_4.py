import random
import milestone_3 as ms3

class Hangman:

    def __init__(self):
        self.word_list = ms3.word_list
        self.num_lives = 5
        self.word = list(random.choice(self.word_list).lower())
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f'Good guess!! {self.guess} is in the word')
            for i, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[i] = letter
                    print(f'Your word so far is: {self.word_guessed}')
                else:
                    self.num_lives -= 1
                    print(f'Sorry {self.letter} is not in the word')
                    print(f'You have {self.num_lives} left')

            self.num_letters -= 1



    def ask_for_input(self):
        while True:
            self.guess = input('Please enter a letter: ').lower()

            if self.guess.isalpha() == False:
                print('Invalid letter. Please enter a single alphabetical letter')
                continue
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter!')
                continue
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                

hangman = Hangman()

print(hangman.ask_for_input())



        