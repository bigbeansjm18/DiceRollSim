import sys

print("Welcome to Dice Rolling Sim!")
print("Type roll followed by your desired max number to roll the dice.")
print("Or you can just type roll and it will use a regular 6 sided die.")

firstAct = input("Type roll to start or quit to exit.")
#roll function
if firstAct == "roll":
    print("rolled")
    
#quit function
elif firstAct == "quit":
    print("Exiting DRS!")
    sys.exit(0)
else:
    print("Type roll to start or quit to exit.")