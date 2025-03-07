function getWorkoutDescription() {
    let userInput = document.getElementById("userInput").value;
    let responseBox = document.getElementById("workoutResponse");

    // Hide response box initially
    responseBox.style.display = "block";
    responseBox.innerText = "Please wait...";

    fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userInput })
    })
    .then(response => response.json())
    .then(data => {
        responseBox.innerText = data.response;
    })
    .catch(error => {
        responseBox.innerText = "Error getting response.";
        console.error("Error:", error);
    });
}

function getMotivation() {
    let responseBox = document.getElementById("motivationResponse");

    // Hide response box initially
    responseBox.style.display = "block";
    responseBox.innerText = "Please wait...";

    fetch("/motivation", {
        method: "POST",
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        responseBox.innerText = data.response;
    })
    .catch(error => {
        responseBox.innerText = "Error getting response.";
        console.error("Error:", error);
    });
}

// Hide response boxes when the page loads
window.onload = function() {
    document.getElementById("workoutResponse").style.display = "none";
    document.getElementById("motivationResponse").style.display = "none";
};
