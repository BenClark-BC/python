"""Rock, Paper, Scissors in Python. This program will ask for user input for their choice of Rock, Paper, or Scissors, and will also assign the computer a random value, then declare (print) the winner."""

from random import randint
from time import sleep

options = ["R", "P", "S"]

you_lose = "You lost, or you possibly broke the game!"
you_win_rock = "Congrats, you win, ROCK Smash puny Scissors! CRUNCH!!"
you_win_scissors = "Congrats, you win, Scissors slice through paper! SNIP!!"
you_win_paper = "Congrats, you win, Paper smothers silly Rock!!"
you_lose_rock = "You lost! Your puny Scissors got smashed by the ROCK! CRUNCHOLA!!"
you_lose_scissors = "You lost, your paper is shredded to ribbons! SNIP SNIP!"
you_lose_paper = "You lost, your poor little rock is enveloped by the insidiously blanket-like paper!! CRUMPLE!!"
invalid_choice = "What have you done? How can you break Rock, Paper, Scissors??? Try again!"


def decide_winner(user_choice, computer_choice):
    print "You chose %s." % user_choice
    print "Computer selecting..."
    sleep(1)
    print "'Puter chose %s." % computer_choice
    sleep(1)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a tie!"
    elif user_choice_index == 0 and computer_choice_index == 2:
        print you_win_rock
    elif user_choice_index == 2 and computer_choice_index == 1:
        print you_win_scissors
    elif user_choice_index == 1 and computer_choice_index == 0:
        print you_win_paper
    elif user_choice_index > 2:
        print invalid_choice
        return
    elif computer_choice_index == 0 and user_choice_index == 2:
        print you_lose_rock
    elif computer_choice_index == 2 and user_choice_index == 1:
        print you_lose_scissors
    elif computer_choice_index == 1 and user_choice_index == 0:
        print you_lose_paper
    else:
        print you_lose


def play_RPS():
    print "Welcome to Rock, Paper, Scissors!"
    sleep(1)
    print "Choose your weapon! Rock, Paper, or Scissors!"
    user_choice = raw_input("Choose R, P, or S: ").upper()
    computer_choice = options[randint(0, len(options) - 1)]
    decide_winner(user_choice, computer_choice)


play_RPS()
