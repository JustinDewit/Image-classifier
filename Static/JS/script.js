function classifyImage() {
    const formData = new FormData(document.getElementById('upload-form'));
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const result = data.prediction;
        const image = document.getElementById('uploaded-image');
        const resultText = document.getElementById('resultText');
        const resultContainer = document.querySelector('.result-container');

        image.src = URL.createObjectURL(document.getElementById('fileInput').files[0]);
        
        resultText.textContent = `This is a ${result}.`;
        
        resultContainer.style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}
