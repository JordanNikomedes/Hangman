import random



class Hangman:
""" This is my hangman class consisting of all the rules and functions
for the game. I have initiated the attributes to use throughout the class  """
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))


    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            
            for i, letter in enumerate(self.word):
                if self.guess == letter:
                    self.word_guessed[i] = letter
                    print(f'Good guess!! {self.guess} is in the word')
                    print(f'Your word so far is: {self.word_guessed}')
                    
                elif self.guess != letter:
                    self.num_lives -= 1
                    print(f'Sorry {self.guess} is not in the word')
                    print(f'You have {self.num_lives} lives left')
                    break
                    
            self.num_letters -= 1
""" In this method i checked if the letter is in the word using a for loop to break
down the word and an if statement to judge what action to take """
                

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
                break


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print('You Lost!!!')
            break

        elif game.num_letters > 0:
            game.ask_for_input()
            continue

        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congratulations, You won the game!!!')
            break
""" This function is calling the hangman class with an if statement to end the game """


if __name__ == '__main__':
    word_list = ['apple', 'grapes', 'hello', 'people', 'cars']
    play_game(word_list)
