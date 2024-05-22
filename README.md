# Hangman

## Description

This project is based on the game hangman where players try and guess the word before the hangman is fully drawn.

The code starts by picking a word at random that is not visible to the player. The player then enters letters to try and guess what that word is. The player has five lives in total. The program judges whether that letter is in the word or not. If that letter is in the word the code will add that letter to the word so the player can see where it is placed. This goes on until the player either guesses the word or runs out of lives.

## Milestone 2

In milestone 2 I started by creating a list of words and randomizing the word chosen by the program. I imported the random library, then created an if statement to check if the input from the user is a valid letter.

## Milestone 3

In milestone 3 I developed the program a bit more by adding the function check guess where I created an if statement to check if the letter is in the word, if it was then a message would be printed to the terminal.



## Milestone 4

In milestone 4 the code is set out in an object oriented program. Below is all the arguments initiated from the class.

![Initialised variables](image.png)

There are two methods within the class. One of them checks if the guess is sucessful presenting a message to let the user know.



The other method asks for the users input with a if statement to check if the input is valid.

![user input method](image-1.png)

The check guess method has been updated so if the user gets a letter correct it would update the hidden word and made it visible to the user. If the letter is wrong then the number of lives gets updated and a message is printed to the user letting them know how many lives they have left.

![Updated check guess method](image-2.png)


## Milestone 5

In milestone 5 I have added a play game function so the program can judge whether to continue the game or judge whether the user has won or lost. I called the hangman class within the function then wrote an if statement to account for the amount of letters left and to check the number of lives left.

![play game function](image-3.png)


## Installations

This python program uses standard libraries, so there are no external installations required. 

## Motivation

My motivation for creating this python program is to practice and to get used to using classes and getting the hang of using python basics to build a bigger program.
