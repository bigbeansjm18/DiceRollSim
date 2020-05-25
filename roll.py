import sys
import random

print("Welcome to Dice Rolling Sim!")
print("Type roll followed by your desired max number to roll the dice.")
print("Or you can just type roll and it will use a regular 6 sided die.")
defaultMin = 1
defaultMax = 6
firstAct = input("Type roll to start or roll set to roll with a max value you can set yourself.")
while firstAct == "roll":
    print("The dice is rolling! Your number is...")
    print(random.randint(defaultMin, defaultMax))
    firstAct = input("Type roll to start or roll set to roll with a max value you can set yourself.")
while firstAct == "roll set":
    userMax = input("Please input the max number you want to use!")
    print("The dice is rolling! Your number is...")
    print(random.randint(defaultMin, int(userMax)))
    firstAct = input("Type roll to start or roll set to roll with a max value you can set yourself.")