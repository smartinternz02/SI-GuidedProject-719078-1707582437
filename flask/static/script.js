function predictPrice() {
    const dateInput = document.getElementById("dateInput");
    const predictionResult = document.getElementById("predictionResult");
    
    const date = dateInput.value;
    
    if (date === "") {
        predictionResult.textContent = "Please enter a date.";
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `Date=${date}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data === "Date not found in forecast data.") {
            predictionResult.textContent = "COuld not Predict the Price";
        } else {
            predictionResult.textContent = `Predicted Price: $${data}`;
        }
    })
    .catch(error => {
        console.error(error);
        predictionResult.textContent = "An error occurred.";
    });
}
