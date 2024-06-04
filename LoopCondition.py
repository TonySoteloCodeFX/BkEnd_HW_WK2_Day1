# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).

from art import leaf, itachi, naruto

should_continue = True
while should_continue:
    print("=" * 100,"\n")
    print("What is the best Anime ever created?\nBe honest and don't lie!\nHere's a clue:\n",leaf)
    answer = input().lower()
    if answer != "naruto":
        print("=" * 100,"\n")
        print("BE HONEST With YOURSELF and DON'T LIE!!!\n")
        print("Here's another clue!\n",itachi)
    else:
        print("=" * 100)
        print(naruto)
        print("Yup that's correct! I'm glad you got it the first time :)")
        should_continue = False

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

iteration = 0
while iteration < 5:
    iteration += 1
    print("This is iteration:", iteration)

