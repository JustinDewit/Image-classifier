from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('Models/your_model_name.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']

    # If user does not select file, browser also submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Convert the file to an image array and make a prediction
    image = tf.keras.preprocessing.image.load_img(file, target_size=(224, 224)) # You may need to adjust the target size based on your ResNet input size
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = tf.expand_dims(image_array, axis=0)
    
    predictions = model.predict(image_array)
    # Translate predictions to your classes
    classes = ['cat', 'dog', 'bird']
    predicted_class = classes[int(predictions[0][0])]

    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
