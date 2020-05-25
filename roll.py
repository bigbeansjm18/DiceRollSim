import sys
import random

print("Welcome to Dice Rolling Sim!")
print("Type roll followed by your desired max number to roll the dice.")
print("Or you can just type roll and it will use a regular 6 sided die.")
defaultMin = 1
defaultMax = 6
firstAct = input("Type roll to start or quit to exit.")
#roll function
if firstAct == "roll":
    print("The dice is rolling! Your number is...")
    print(random.randint(defaultMin, defaultMax))
    