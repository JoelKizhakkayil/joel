// Add event listener to the submit button near the search bar
document.querySelector('.button').addEventListener('click', function(event) {
    // Prevent the default action of the button (like submitting the form)
    event.preventDefault();

    // Open a new tab
    const newTab = window.open();
    let countdown = 5; // Countdown starts at 5 seconds

    // Write initial content to the new tab, including the countdown
    newTab.document.write(`
        <html>
            <head>
                <title>Under Construction</title>
            </head>
            <body style="text-align: center; margin-top: 100px;">
                <h1>Search feature still under construction!</h1>
                <h4>Please check back later.</h4>
                <h4>Tab closing in <span id="countdown">${countdown}</span> seconds...</h4>
            </body>
        </html>
    `);

    // Update the countdown every second
    const intervalId = setInterval(() => {
        countdown--; // Decrement the countdown
        newTab.document.getElementById('countdown').textContent = countdown; // Update the countdown in the new tab
        
        if (countdown <= 0) {
            clearInterval(intervalId); // Stop the countdown
           setTimeout(() => {newTab.close()
           }, 2000); newTab.close(); // Close the tab
        }
    }, 1000);
});