# Task 1: Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

import random

nums = range(1,11)
secret_num = random.choice(nums)

should_continue = True

while should_continue:
    print("=" * 50)
    guess = int(input("Guess a number between 1 - 5\n"))
    if guess > secret_num:
        print("=" * 50)
        print("Lower\n")
        print("=" * 50)
    elif guess < secret_num:
        print("=" * 50)
        print("Higher\n")
        print("=" * 50)
    else:
        print("=" * 50)
        print("You guessed it! The Mystery Number was:", secret_num)
        print("=" * 50)
        should_continue = False
