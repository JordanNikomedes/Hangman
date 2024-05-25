import random



class Hangman: 
    """ Hangman game that emulates the physical game """
    def __init__(self, word_list, num_lives=5):
        """ initiates the attributes throughout the class

        Parameters
        ----------
        word_list : list
            a list of words randomized by the program 
        num_lives : int
            the number of lives a user has to guess the word correctly, by default 5
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))


    def check_guess(self, guess):
        """ The check guess method breaks down the word and checks if the guess
        is equal to one of the letters inside the word.

        Parameters
        ----------
        guess : string
            this is inputed by the user which loops through to check what statement it meets.
        """
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

                

    def ask_for_input(self):
        """ Asks user to input a valid letter, loops through to check if
            the letter is already guessed. Once checked the check guess method
            is called and is added to list of guesses. 
        """
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
    """ calls the hangman class and loops through to judge whether to end the game.

    Parameters
    ----------
    word_list : list
        a list is passed to initiate the start of the game
    """
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



if __name__ == '__main__':
    word_list = ['apple', 'grapes', 'hello', 'people', 'cars']
    play_game(word_list)
