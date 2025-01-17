document.getElementById('prediction-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    try {
        // Display a loading spinner
        const spinner = document.getElementById('loading-spinner');
        spinner.style.display = 'block';

        // Send the data to the backend
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        spinner.style.display = 'none'; // Hide spinner after response is received

        const resultDiv = document.getElementById('result');
        if (result.error) {
            resultDiv.textContent = `Error: ${result.error}`;
            resultDiv.style.color = 'red';
        } else {
            resultDiv.textContent = `Predicted AQI: ${result.predicted_aqi}`;
            resultDiv.style.color = 'green';
        }
    } catch (error) {
        // Hide spinner and show error if any network or unexpected issue occurs
        document.getElementById('loading-spinner').style.display = 'none';
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = `Error: Unable to process your request. Please try again later.`;
        resultDiv.style.color = 'red';
    }
});
