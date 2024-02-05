import random

def runMultiple(runAmount):
    # Initialize variables
    simulationAmount = 0
    green_results = []

    red = 0
    black = 0
    green = 0

    # Loop for the specified number of simulations
    while simulationAmount < runAmount:
        
        # Reset color counts for each simulation
        red = 0
        black = 0
        green = 0

        # Print simulation header
        print("\n-----------------------------------------\n")

        # Loop through 100 random numbers representing outcomes
        for i in range(100):
            randomNum = random.randint(1, 15)
            print(f"{simulationAmount + 1:<4}", end='')
            
            # Check the range of the random number and update color counts
            if randomNum >= 1 and randomNum <= 7:
                print(" Red", f"{randomNum:>5}")
                red += 1
            elif randomNum >= 8 and randomNum <= 14:
                print("Black", f"{randomNum:>4}")
                black += 1
            else:
                print("Green", f"{randomNum:>4}")
                green += 1
        
        # Increment simulation count and store green count for the simulation
        simulationAmount += 1
        green_results.append(green)
        
    # Print overall results after all simulations
    print("\nRed: ", red, "\nBlack: ", black, "\nGreen", green)
    print("\nThe amount of simulations run was", simulationAmount)

    # Find and print maximum and minimum green counts in any simulation
    max_green = max(green_results)
    min_green = min(green_results)
    print("\nThe highest green amount in a simulation was:", max_green)
    print("The lowest green amount in a simulation was:", min_green)

    # Calculate and print the average green count across all simulations
    average_green = sum(green_results) / len(green_results)
    print("The average green amount was:", average_green)


