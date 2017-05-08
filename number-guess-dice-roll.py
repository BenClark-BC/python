'''This Python game will have the user guess the result of rolling a pair of dice. If the user's guess is higher than the dice roll, the user wins. I'll hopefully be able to covert this into a D&D Dice Rolling game.'''

from random import randint

from time import sleep

def get_user_guess():
    user_guess = int(raw_input("Guess the outcome of the roll of two dice:"))
    return user_guess

def get_number_of_sides():
    number_of_sides = int(raw_input("Choose the number of sides the dice will have:"))
    return number_of_sides

num_sides = get_number_of_sides()

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = 2 * number_of_sides
    print "The maximum value of the roll can add up to is %s" % str(max_val)
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "Invalid number, the chosen number exceeds the max value."
        return
    elif user_guess < 2:
        print "Invalid number, the chosen number is lower then the minimum value."
        return
    else:
        print "Rolling the dice!!!"
        sleep(1)
        print "Tumble! Clunk! Rattle!"
        sleep(1)
        print "Die one: %d" % first_roll
        sleep(1)
        print "Die two: %d" % second_roll
        sleep(1)
        print "Adding values together..."
        sleep(1)
        total_roll = first_roll + second_roll
        print "Result..."
        sleep(1)
        if user_guess > total_roll:
            print "You won! Your guess was %d, and the roll was %d" % (user_guess, total_roll)
            return
        else:
            if user_guess <= total_roll:
                print "Sorry, your guess of %d was less than or equal to the actual roll of %d. The robots have won and will now take over the world." % (user_guess, total_roll)
        return

roll_dice(num_sides)
