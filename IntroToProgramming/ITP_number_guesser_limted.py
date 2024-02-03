'''
number_guesser_simplified.py is a game where the user gets five guesses to guess a number between 1 and 100
randomly chosen by the random python module.
'''

import random  # imports the random module

num = random.randint(1, 100)  # selects a random number between 1 and 100
count = 0  # sets the count variable to 0

while count < 5:  # start a while loop to continue until max guesses of 5 reached
    try:  # start try block to catch exceptions
        user_input = int(input('Guess a number between 1 and 100: '))  # user prompt to enter guess

        if 1 <= user_input <= 100:  # checks if user number within the valid range of 1 to 100 inclusive
            count += 1  # increase counter by 1 when a valid guess is entered by user
            if user_input < num:  # checks if user guess is lower than random number
                print("The number is higher than your guess.")  # message to direct user to guess higher
            elif user_input > num:  # checks if user guess is higher than random number
                print("The number is lower than your guess.")  # message to direct user to guess lower
            else:  # checks if user guess is correct
                print("CORRECT!")  # displays message when guess matches number
                print('Number of guesses =',count)  # displays number of guesses
                break  # exits the while loop when guess is correct
        else:  # error handling if number not between 1 and 100 inclusive
            print("Please enter a number between 1 and 100.")  # try again message

    except ValueError:  # exception handling if user entry is not an integer
        print("That's not a valid number. Please try again.")  # try again message

if count == 5:  # checks if guesses count has reached max
    print("Max guesses reached - game over!")  # displays game over message if max guesses reached
