# Cat, dog, Bird Image Classifier
#### Video Demo:  <https://www.youtube.com/watch?v=hWQxfbtyTk8>
#### Description: This Image Classifier Web App seamlessly integrates Flask and TensorFlow's ResNet50 to accurately categorize uploaded images as cats, dogs, or birds.

An interactive web application that allows users to upload images and receive predictions on whether the image contains a cat, dog, or bird, utilizing a deep learning model built on TensorFlow's ResNet architecture.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- User-friendly interface for image uploads.
- Real-time image classification using a pre-trained deep learning model.
- Displays the prediction as cat, dog, or bird.

## Getting Started

### Prerequisites

- Python 3.11.6
- Flask
- TensorFlow
- Pillow

### Installation

1. Clone the repo:
```bash
git clone https://github.com/JustinDewit/Image-classifier.git
```

2. Navigate to the project directory:
```bash
cd Image-classifier
```

3. Create a virtual environment:
```bash
python -m venv venv
```

4. Activate the virtual environment:
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

5. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Project Structure

- `train.py` - Script used for training the ResNet model on the dataset.
- `app.py` - Flask application for serving predictions.
- `Models/` - Contains the pre-trained deep learning model.
- `Dataset/` - Directory containing the categorized images used for training and validation.
- `templates/` - (if implemented later) Contains the HTML templates for the web application.
- `static/` - (if implemented later) Contains the CSS, JS, and other static assets.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- TensorFlow and the ResNet model.
- Flask for making the backend integration possible.
- [Kaggle](https://www.kaggle.com/) for the dataset.