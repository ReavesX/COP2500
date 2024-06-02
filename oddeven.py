# Donald Jackson - oddeven.py - Uses the rnd function to choose a number
# then asks for a guess as to whether its odd or even from the user. Depending
# whether or not they guess correctly a message will be printed out.


# importing the random library,and using the casefold
# function to set the user's input to a single case
import random
myNumber = random.randint(1,256)
userGuess = (input("Let's play a game, is my number odd or even?")).casefold()

# Conditional statements to determine if the number was even or odd by dividing and checking for divisibility by 2.

if myNumber % 2 == 0 and userGuess == "even":
    print("You Guessed Correct.","The number was:",myNumber)
elif myNumber %2 != 0 and userGuess == "odd":
    print("You Guessed Correct.","The number was:",myNumber)
else:
    print("You've forfeited the game by not entering odd or even.","The number was:",myNumber)
