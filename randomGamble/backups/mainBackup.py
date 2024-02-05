import random
import math
import sys

# Add the path to the module to the system path
sys.path.append('C:\\Users\\sdbru\\Coding')

# Import the 'runMultiple' function from the 'simulation' module
from randomGamble.simulation import runMultiple

# Initial player amount
playerAmount = 100

def gamble(gambleAmount, gambleColor):
    # Access the global player amount
    global playerAmount

    # Generate a random number representing the outcome
    randomNum = random.randint(1, 15)

    # Check the outcome and update the player's amount accordingly
    if randomNum >= 1 and randomNum <= 7:
        print("Red")
        if gambleColor == "red":
            playerAmount += (gambleAmount * 2.1)
        else:
            playerAmount += 0
    elif randomNum >= 8 and randomNum <= 14:
        print("Black")
        if gambleColor == "black":
            playerAmount += (gambleAmount * 2.1)
        else:
            playerAmount += 0
    else:
        print("Green")
        if gambleColor == "green":
            playerAmount += (gambleAmount * 14.7)
        else:
            playerAmount += 0

    playerAmount = math.floor(playerAmount)
    print("Your new amount is: ", playerAmount)

def getGamble():
    # Access the global player amount
    global playerAmount
    betValid = False

    # Get the bet amount from the user, ensuring it is valid
    while not betValid:
        print("You have ", playerAmount, " tokens, how many would you like to wager? ")
        betAmount = int(input())
        if betAmount <= playerAmount:
            betValid = True
            playerAmount -= betAmount
            return betAmount
        else:
            print("Invalid bet. Please enter a valid amount.")

# Main loop for continuous gambling
while True:
    gamble(getGamble(), input("Enter a color: "))

#runMultiple(int(input("Enter how many times you would like to run the simulation?: ")))
