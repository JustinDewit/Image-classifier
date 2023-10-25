# Imports
import os
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense

# 1. Load Pre-trained ResNet Model without Top Layer
base_model = ResNet50(weights='imagenet', include_top=False)

# 2. Data Preparation using ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

val_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Dataset/train',
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')

validation_set = val_datagen.flow_from_directory('Dataset/validation',
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')

# For simplicity, let's say you have 3 classes (e.g., cat, dog, bird). Adjust this based on your categories.
num_classes = 3

# 3. Add custom layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Freeze initial layers of ResNet
for layer in base_model.layers:
    layer.trainable = False

# 4. Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. Train the model
model.fit(training_set, validation_data=validation_set, epochs=10)  # Adjust epochs as needed

# 6. Save the trained model
model_path = os.path.join('Models', 'custom_resnet_model.h5')
model.save(model_path)

print(f"Model saved at {model_path}")
