# Import necessary modules from Flask and custom modules
from flask import Flask, render_template, request, jsonify
from randomGamble.simulation import runMultiple  # Import from another python file

# Import Python standard libraries
import random
import math

# Create a Flask web application instance
app = Flask(__name__)

# Initial player amount
playerAmount = 9.57

# Function to simulate the gambling process
def gamble(gambleAmount, gambleColor):
    global playerAmount

    # Simulate a random result with specified color and multiplier
    randomNum = random.randint(1, 15)
    color = ""
    multiplier = 0

    if randomNum >= 1 and randomNum <= 7:
        color = "Red"
        multiplier = 2.1
    elif randomNum >= 8 and randomNum <= 14:
        color = "Black"
        multiplier = 2.1
    else:
        color = "Green"
        multiplier = 14.7

    # Check if the guessed color matches the simulated result
    if gambleColor == color.lower():
        # Update player's balance based on the result
        playerAmount += gambleAmount * multiplier - gambleAmount
        message = f"You guessed the correct color: {color}"
    else:
        # Deduct bet amount from player's balance for incorrect guess
        playerAmount -= gambleAmount
        message = f"You guessed the wrong color. The correct color was: {color}"

    # Ensure playerAmount is rounded down to the nearest 2nd decimal place
    playerAmount = math.floor(playerAmount * 100) / 100
    playerAmount = max(playerAmount, 0)  # Ensure playerAmount doesn't go below 0

    # Return result data
    return {"color": color, "amount": playerAmount, "message": message}

# Define a route for the home page
@app.route('/')
def index():
    # Render the main page with the current player balance
    return render_template('index.html', balance=playerAmount)

# Define a route for placing bets
@app.route('/place_bet', methods=['GET'])
def place_bet():
    # Retrieve the bet amount and color from the request parameters
    betAmountStr = request.args.get('amount')
    betColor = request.args.get('color')

    try:
        # Convert the bet amount to a float and round down to the nearest 2nd decimal place
        betAmount = math.floor(float(betAmountStr) * 100) / 100

        # Check if the bet amount exceeds the available player balance
        if betAmount > playerAmount:
            responseData = {
                "error": f"Invalid bet. Bet amount ({betAmount}) exceeds available balance ({playerAmount}).",
            }
        else:
            # Simulate the gambling process and update the player's balance
            result = gamble(betAmount, betColor)
            responseData = {
                "color": result['color'],
                "amount": math.floor(result['amount'] * 100) / 100,  # Ensure amount is rounded down to the nearest 2nd decimal place
                "message": result['message']
            }
    except ValueError:
        # Handle the case where the bet amount is not a valid number
        responseData = {
            "error": "Invalid bet amount. Please enter a valid number."
        }

    # Return the result data in JSON format
    return jsonify(responseData)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
