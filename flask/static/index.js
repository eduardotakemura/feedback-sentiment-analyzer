document.getElementById('analyzeButton').addEventListener('click', function() {
    const message = document.querySelector('.message-box').value;

    if (message.trim() === "") {
        alert("Please enter a message.");
        return;
    }

    // Show the spinner and hide results while waiting for the backend
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('resultBox').style.display = 'none';

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        // Hide the spinner once the response is received
        document.getElementById('loadingSpinner').style.display = 'none';

        // Update the sentiment and emotion scores in the UI
        document.getElementById('sentimentScore').textContent = (data.sentiment[0].score * 100).toFixed(2);
        document.getElementById('sentimentLabel').textContent = data.sentiment[0].label.replace('LABEL_', '');
        document.getElementById('emotionScore').textContent = (data.emotion[0].score * 100).toFixed(2);
        document.getElementById('emotionLabel').textContent = data.emotion[0].label;

        // Display the result box
        document.getElementById('resultBox').style.display = 'block';

        // Optionally update progress bars
        updateProgressBar('sentimentProgress', data.sentiment[0].score * 100);
        updateProgressBar('emotionProgress', data.emotion[0].score * 100);
    });
});

function updateProgressBar(barId, value) {
    const progressBar = document.getElementById(barId);
    progressBar.style.width = value + '%';
}

