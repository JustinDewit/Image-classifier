import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the trained model
MODEL_PATH = 'Models/custom_resnet_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Create an ImageDataGenerator instance for test data
test_datagen = ImageDataGenerator(rescale=1./255)

# Load the test data
test_set = test_datagen.flow_from_directory('Dataset/test',
                                            target_size=(224, 224),
                                            batch_size=32,
                                            class_mode='categorical',
                                            shuffle=False)  # Set shuffle to False for consistent evaluation

# Evaluate the model on the test data
loss, accuracy = model.evaluate(test_set)

# Print the evaluation results
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    pass  # The evaluation logic has already been executed at the top level.
