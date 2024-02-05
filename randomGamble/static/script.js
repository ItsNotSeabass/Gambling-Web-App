// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener("DOMContentLoaded", function() {

    // Function to handle placing a bet
    function placeBet() {
        // Get the bet amount and color from the respective input fields
        const betAmount = document.getElementById("betAmount").value;
        const betColor = document.getElementById("betColor").value;

        // Make a fetch request to the server to place the bet with the provided amount and color
        fetch(`/place_bet?amount=${betAmount}&color=${betColor}`)
            .then(response => response.json()) // Parse the response as JSON
            .then(data => {
                // Check for errors in the response data
                if (data.error) {
                    // Display the error message in the result element
                    document.getElementById("result").innerText = data.error;
                } else {
                    // Display the success message in the result element
                    document.getElementById("result").innerText = data.message;

                    // Set the text color of the result element based on the color received from the server
                    document.getElementById("result").style.color = data.color.toLowerCase();

                    // Update the displayed balance with the returned amount, rounded to two decimal places
                    document.getElementById("balance").innerText = `${data.amount.toFixed(2)}`;
                }
            })
            .catch(error => console.error('Error:', error)); // Handle any fetch errors
    }

    // Add an event listener to the "Place Bet" button to trigger the placeBet function on click
    document.getElementById("placeBetButton").addEventListener("click", placeBet);
});
