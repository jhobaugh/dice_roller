
'''
1. Dice Rolling Simulator
The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice.
When the program runs, it will randomly choose a number between 1 and 6.
(Or whatever other integer you prefer — the number of sides on the die is up to you.)
The program will print what that number is.
It should then ask you if you’d like to roll again.
For this project, you’ll need to set the min and max number that your dice can produce.
For the average die, that means a minimum of 1 and a maximum of 6.
You’ll also want a function that randomly grabs a number within that range and prints it.'''

import random

looper = True

while looper:
    sides = int(input("Thanks for using dice roll!\nHow many sides on your dice? "))
    dice = random.randrange(1, sides)
    print(dice)
    answer = str(input("Would you like to roll again? "))
    if answer == "no":
        looper = False

print("Have a great day!")